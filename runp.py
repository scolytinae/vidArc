from vidarc import app
from vidarc.src.loggers import add_loggers

add_loggers(app)
app.logger.info('run application')
app.run(debug=False)
