# 스파르타 코딩 클럽 6기 수업자료

## 템플릿으로 시작하기

1. 에디터에서 새 파일을 생성합니다.
2. **부트스트랩을 사용하기**: [bootstrap](https://getbootstrap.com/) 사이트에서 `Get Started` 에 있는 `Starter template`을 복사합니다.
3. **제이쿼리 사용하기**: [jquery cdn](https://code.jquery.com/) 사이트에서 3.x 버전의 minified 버전 스크립트를 복사합니다.
4. 위 2번에서 가져온 템플릿의 스크립트에서 jquery 부분을 바꿔치기 합니다.

> **왜?**  
> 부트스트랩에 있는 jqeury 는 slim 버전으로 ajax 기능이 빠져 있습니다.  
> ajax 기능을 사용하기 위해서 slim 버전이 아닌것으로 대체하는 것입니다.

**✅ 최종파일**(이걸 복사하시면 됩니다.)  
```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>
```

---

