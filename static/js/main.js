$(function(){
    if ('speechSynthesis' in window && window.location.pathname.indexOf("aural") >= 0) {
        $('.flashcard').click(function(e){
            e.preventDefault();
            target = $(e.currentTarget);
            checkbox = target.find('input')[0];
            if (!checkbox.checked) {
                var text = target.find('.back')[0].innerText;
            } else {
                var text = target.find('.front')[0].innerText;
            }
            
            var msg = new SpeechSynthesisUtterance();
            msg.text = text;
            checkbox.checked = !checkbox.checked;
            speechSynthesis.speak(msg);
        })
    }
});