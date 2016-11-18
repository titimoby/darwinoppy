<p>List of all motors scanned</p>
<table border="1">
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
    <td>{{motors[motor]['position']}}</td>
  </tr>
%end
</table>
