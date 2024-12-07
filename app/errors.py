def register_errors(app):
  @app.errorhandler(404)
  def page_not_found(error):
    return """
          <h1 style="color: red;">404: Página no encontrada</h1>
          <p>Lo sentimos, pero la página que buscas no existe. 🙁</p>
      """, 404

  @app.errorhandler(500)
  def error_500(error):
    return "<h1>Error 500: Algo salió mal 🤯</h1>", 500

  @app.errorhandler(403)
  def acceso_denegado(error):
      return """
          <h1 style="color: purple;">403: Acceso denegado</h1>
          <p>No tienes permiso para acceder a esta página. 🚫</p>
      """, 403