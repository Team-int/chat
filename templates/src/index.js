$(document).ready(function () {
  var serverIcon = $("img").filter("#server_icon");
  $(serverIcon).on("click", function (event) {
    var serverID = $(this).parent().data("serverId");
    console.log("Server ID: " + serverID);
  });
});
