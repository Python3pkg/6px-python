class Output:
    def __init__(self, refs):
        self.hasFilters = False
        self.actions = []
        self.filters = {}
        self.type = 'image/png'
        self.location = None
        self.tagName = None
        self.refs = refs

        self.data = {}

    def tag(self, tag):
        """
        Sets the tag for our input image
        """

        self.tagName = tag

        return self

    def resize(self, size):
        """
        Sets an action to our image to resize given the width and height given
        """

        self.data['resize'] = dict(list(self.data.get('resize', {}).items()) + list(size.items()))

        return self

    def filter(self, type, value):
        """
        Sets image filters to our image
        """

        self.hasFilters = True

        self.filters[type] = value

        return self

    def rotate(self, options):
        """
        Rotates our input image
        """

        self.data['rotate'] = dict(list(self.data.get('rotate', {}).items()) + list(size.items()))

        return self

    def url(self, location):
        self.location = location

        return self

    def crop(self, position):
        """
        Crops our image to given coordinates or to the dominate face
        """

        self.data['crop'] = dict(list(self.data.get('crop', {}).items()) + list(position.items()))

        return self

    def export(self):
        """
        Generates the dictionary needed for this output
        """

        if self.hasFilters:
            self.actions.append({ 'method': 'filter', 'options': self.filters })

        for (index, options) in list(self.data.items()):
            self.actions.append({
                'method': index,
                'options': options
            })

        output = {
            'ref': self.refs,
            'type': self.type,
            'tag': self.tagName,
            'methods': self.actions
        }

        if self.location:
            output['url'] = self.location

        return output;
