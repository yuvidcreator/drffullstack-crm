import json

from rest_framework.renderers import JSONRenderer


class EmployeeJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get("errors", None)

        if errors is not None:
            return super(EmployeeJSONRenderer, self).render(data)

        return json.dumps({"employee": data})



class CustomerJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get("errors", None)

        if errors is not None:
            return super(CustomerJSONRenderer, self).render(data)

        return json.dumps({"customer": data})
