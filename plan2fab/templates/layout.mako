<!DOCTYPE html>
<html lang="fr">
<head>
  <title>Plan 2 Fab - Documentation de projet de fabricaqtion</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="${request.static_url('plan2fab:static/style.css')}" type="text/css" media="screen" />
  <!--[if lte IE 6]>
  <link rel="stylesheet" href="${request.static_url('plan2fab:static/ie6.css')}" type="text/css" media="screen" />
  <![endif]-->
</head>
<body>
  <header>
  <h1>Plan 2 Fab<h1>
  <img src="${request.static_url('plan2fab:static/ecodesignfablab.jpg')}" alt="écodesignfablab"/>
  </header>
  <div>
    ${self.body()}
  <div>
</body>
</html>
