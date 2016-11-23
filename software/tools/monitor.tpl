<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Darwinoppy settings</title>

<!-- Bootstrap from CDN -->
<!-- Latest compiled and minified CSS -->
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

<p>List of all motors scanned</p>
<table class="table">
  <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Detected?</th>
    <th>Position</th>
  </tr>
%for motor in motors:
  <tr>
    <td>{{motors[motor]['id']}}</td>
    <td>{{motors[motor]['name']}}</td>
    <td>{{motors[motor]['detected']}}</td>
    <td><div class="input-group">
          <span class="input-group-btn">
              <button type="button" class="btn btn-danger btn-number"  data-type="minus" data-field="">
                <span class="glyphicon glyphicon-minus"></span>
              </button>
          </span>
          <input type="text" name="quant[2]" class="form-control input-number" value="{{motors[motor]['position']}}">
          <span class="input-group-btn">
              <button type="button" class="btn btn-success btn-number" data-type="plus" data-field="">
                  <span class="glyphicon glyphicon-plus"></span>
              </button>
          </span>
      </div></td>
  </tr>
%end
</table>

</body>
</html>
