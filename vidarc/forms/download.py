from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError


class DownloadForm(Form):
    address = StringField('address', validators=[DataRequired()])

    def validate_address(self, field):
        if field.data != 'test':
            raise ValidationError('field data must be "test"')