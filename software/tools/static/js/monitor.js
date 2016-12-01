function incrementServoPosition() {
      $.ajax({
      url: 'http://localhost:8066/incrementServoPosition',
      data: {
         id: '3'
      },
      error: function() {
         console.log("error")
      },
      dataType: 'jsonp',
      success: function(data) {
         console.log("success")
      },
      type: 'GET'
   });
}
