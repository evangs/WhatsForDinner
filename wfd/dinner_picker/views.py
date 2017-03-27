from dinner_picker.forms import PreferenceForm
from django.views.generic.edit import FormView
from django.conf import settings

import requests as r
import googlemaps
import math

class FindFoodView(FormView):
    template_name = 'findfood.html'
    form_class = PreferenceForm
    success_url = '/'

    def form_valid(self, form):

        keyword = form.cleaned_data['keyword'] or ''
        gmap = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        data = gmap.places_nearby((form.cleaned_data['latitude'], form.cleaned_data['longitude']), keyword=keyword, open_now=False, rank_by='distance', type='restaurant')

        price_level = form.cleaned_data['price_level']
        minimum_rating = float(form.cleaned_data['minimum_rating'])

        results = data.get('results')

        if results:
            destinations = []
            for result in results:
                loc = result.get('geometry').get('location')
                destinations.append((loc.get('lat'), loc.get('lng')))

            distance_data = gmap.distance_matrix((form.cleaned_data['latitude'], form.cleaned_data['longitude']), destinations, units='imperial')
            distances = distance_data['rows'][0]['elements']
            destinations = distance_data['destination_addresses']

        filtered_results = []

        for index, result in enumerate(results):
            if result.get('opening_hours', {}).get('open_now') and result.get('price_level', 0) <= price_level and result.get('rating', 6) >= minimum_rating and 'lodging' not in result['types']:
                if 'price_level' not in result:
                    result['price_level'] = -1

                if 'rating' not in result:
                    result['rating'] = 0

                result['rating_range'] = [1,2,3,4,5]
                result['price_range'] = [1,2,3,4]

                result['distance'] = distances[index]['distance']['text']
                result['duration'] = distances[index]['duration']['text']
                result['address'] = destinations[index]
                # get photo
                purl = '{base_url}?maxwidth={max_width}&photoreference={photo_ref}&sensor=true&key={api_key}'.format(
                        base_url=settings.PLACE_PHOTO_SERVICE_URL,
                        max_width=400,
                        photo_ref=result['photos'][0]['photo_reference'],
                        api_key=settings.GOOGLE_API_KEY,
                )
                result['photo_url'] = purl

                filtered_results.append(result)

        return self.render_to_response(self.get_context_data(form=form, results=filtered_results))