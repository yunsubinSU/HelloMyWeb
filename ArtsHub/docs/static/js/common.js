// jQuery 코드 실행
loadJQuery(function () {
    
  
    // 헤더랑 푸터 불러오는 제이쿼리
    $(function () {
      $("#header").load("../../pages/public/header.html");
    });
    $(function () {
      $("#footer").load("../../pages/public/footer.html");
    });
  });