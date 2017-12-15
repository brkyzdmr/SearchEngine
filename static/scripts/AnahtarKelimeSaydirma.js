function search() {

  var word = document.getElementById('anahtar_kelime').value;
  var url = document.getElementById('aranacak_url').value;
  console.log(url)
  if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
  }
  else
  {// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
      {
          data = xmlhttp.responseText;
      }
  }
  xmlhttp.open("GET", url, false );
  xmlhttp.send();
  alert(data)
}
