electrician = ['electrician','lights','wiring','socket','power','flickering','flicker','circuit']
plumber = ['plumber','faucet', 'pipe', 'toilet', 'plumbing','leak']
time = ['timely', 'fast', 'quick', 'wait','slow','time','arrived','arrive','come','go','went','going','reliable','wait','efficient','within','convenient','asap','now']
friendly = ['friendly','talked','nice','enjoy','enjoyable','talk','chat','went over','helped','help']
communicative = ['talked','talk','phone','call','called','email','promised','promise','say','said','saying','explain','chat']
quality = ['experience','experienced','well','good','perform','fix','fixed','install','installed','service','recommend',]


$(document).ready(function(){
  $("#search").keyup(function(){
    detectPreference($(this).val());
  })
  $("#submit").click(function(){
    $("#loader").fadeIn(300);
  })
  function detectPreference(str){
    arr = {
      'timely': match(str,time),
      'friendly': match(str,friendly),
      'communicative': match(str,communicative),
      'quality': match(str,quality)
    }
    console.log(arr)
    for(id in arr){
      $('input#'+id).prop('checked', arr[id]);
    }
  }
  function match(str, arr2){
      arr1 = str.toLowerCase().split(' ');
      for(x in arr2){
        if(arr1.includes(arr2[x]))
            return true;
      }
      return false;
  }

})
