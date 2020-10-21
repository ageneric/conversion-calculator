 $('#submit').click(function() {
    console.log(items);
   
    $.ajax({
      type: "POST",
      contentType: "application/json;charset=utf-8",
      url: "/result",
      traditional: "true",
      data: JSON.stringify({items}),
      dataType: "json"
      });
});