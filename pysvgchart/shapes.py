class Point:

    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position


class Shape:

    def __init__(self, x_position, y_position):
        self.position = Point(x_position, y_position)
        self.styles = dict()

    @property
    def render_styles(self):
        return " ".join([style + '="' + self.styles[style] + '"' for style in self.styles])

    def get_element_list(self):
        raise NotImplementedError("Not implemented in generic shape.")


class Line(Shape):
    line_template = '<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {styles}/>'

    def __init__(self, x_position, y_position, width, height, styles=None):
        super().__init__(x_position, y_position)
        self.end = Point(x_position + width, y_position + height)
        self.styles = dict() if styles is None else styles

    @property
    def start(self):
        return self.position

    def get_element_list(self):
        return [self.line_template.format(x1=self.start.x, y1=self.start.y, x2=self.end.x, y2=self.end.y, styles=self.render_styles)]


class Circle(Shape):
    circle_template = '<circle cx="{x}" cy="{y}" r="{r}" {styles}/>'

    def __init__(self, x_position, y_position, radius, styles=None):
        super().__init__(x_position, y_position)
        self.styles = dict() if styles is None else styles
        self.radius = radius

    def get_element_list(self):
        return [self.circle_template.format(x=self.position.x, y=self.position.y, r=self.radius, styles=self.render_styles)]


class Text(Shape):
    text_template = '<text x="{x}" y="{y}" {styles}>{content}</text>'

    def __init__(self, x_position, y_position, content, styles=None):
        super().__init__(x_position, y_position)
        self.styles = dict() if styles is None else styles
        self.content = content

    def get_element_list(self):
        return [self.text_template.format(x=self.position.x, y=self.position.y, content=self.content, styles=self.render_styles)]
