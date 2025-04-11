const toggleBtn = document.querySelector('.navbar_menu');
const depth1 = document.querySelector('.depth1');
const rightside = document.querySelector('.rightside');
console.log(toggleBtn);
console.log(depth1);
console.log(rightside);

 
toggleBtn.addEventListener('click', (e)=>{
    console.log('clicked...',e)
    e.stopPropagation();
    depth1.classList.toggle('active');
    rightside.classList.toggle('active');
});

document.addEventListener('clickleave', (e)=>{

    e.stopPropagation();
    depth1.classList.remove('active');
    rightside.classList.remove('active');
});

depth1.addEventListener('click', (e) => e.stopPropagation());
rightside.addEventListener('click', (e) => e.stopPropagation());
document.addEventListener("DOMContentLoaded",function(){

});
// jQuery 로드 함수
function loadJQuery(callback) {
    if (window.jQuery) {
      callback();
    } else {
      var script = document.createElement("script");
      script.src = "https://code.jquery.com/jquery-3.6.0.min.js";
      script.onload = callback; // jQuery 로드 완료 후 실행
      document.head.appendChild(script);
    }
  }

// 헤더랑 푸터 불러오는 제이쿼리

    loadJQuery(function () {
      $("#header").load("../../pages/public/footer.html");
      $("#footer").load("../../pages/public/footer.html");
    });


  