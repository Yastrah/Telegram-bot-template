from jinja2 import Environment, FileSystemLoader

class TemplateEngine:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_template(self, template_name, **kwargs) -> str:  # probably you can add language Param for localisation
        """
        Render HTML-template with given data
        :param template_name: template name (without file extension)
        :param kwargs: args for substitution
        :return: rendered HTML in form of string
        """
        template = self.env.get_template(f"{template_name}.html")
        return template.render(**kwargs)


template_dir = "templates"
template_engine = TemplateEngine(template_dir)
