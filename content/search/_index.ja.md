---
title: "全てのカテゴリから検索"
draft: false
---
<input id = "query" onkeyup="search(this.value)" size="28" autocomplete="off" autofocus placeholder="検索キーワードを入れてください" />

<script>
    // 検索
    function search(query) {
        $(".card").each(function(i, elem) {
            var question = $(elem).find("span").text().toLowerCase();
            var answer = $(elem).find(".card-body").text().toLowerCase();
            if (query == "" || (question.indexOf(query) == -1 && answer.indexOf(query) == -1)) {
                $(elem).css("display", "none");
            } else {
                $(elem).css("display", "block");
            }
        })
    }
    // ハッシュフラグメントの値で検索を実行
    function searchWithHash() {
        const hash = decodeURI(location.hash.substring(1));
        search(hash);
        // 必要があれば input 要素の値を更新
        const queryElem = document.getElementById('query');
        if (queryElem.value !== hash) {
        queryElem.value = hash;
        }
    }
    // ハッシュフラグメント付きの URL でページを開いたときに検索
    window.addEventListener('DOMContentLoaded', searchWithHash);
    // ページ表示後にハッシュフラグメントが変化したら検索
    window.addEventListener('hashchange', searchWithHash);
</script>

{{< result >}}