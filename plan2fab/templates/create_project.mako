<%inherit file="layout.mako"/>

<p> new project </p>
<form method="post" action="${submit_project_url}">
  <p>
    <label>
      Nom
      <br>
      <input type="text" name="name" />
    </label>
  </p>
  <p>
    <label>
      Description
      <br>
      <textarea name="description"></textarea>
    </label>
  </p>
  <p>
    <label>
      Plan
      <br>
      <input type="file" name="plan" />
    </label>
  </p>
  <p>
    <label>
      Temps estimé
      <br>
      <input type="number" name="duration" />
    </label>
  </p>
  <p>
    <label>
      Matériel
      <br>
      <textarea name="furnitures"></textarea>
    </label>
  </p>
  <p>
    <label>
      Photo object
      <br>
      <input type="file" name="object_image" />
    </label>
  </p>
  <p>
    <label>
      Difficulté
      <br>
      <input type="number" name="difficulty" />
    </label>
  </p>
  <p>
    <label>
      Tags
      <br>
      <textarea name="tags" ></textarea>
    </label>
  </p>
  <p>
    <label>
      Auteurs
      <br>
      <input type="text" name="authors" />
    </label>
  </p>
  <p>
    <label>
      Historique
      <br>
      <textarea name="history"></textarea>
    </label>
  </p>
  <p>
    <label>
      Licence
      <br>
      <input type="text" name="licence" />
    </label>
  </p>
  <p>
    <input type="submit"/>
  </p>
</form>
