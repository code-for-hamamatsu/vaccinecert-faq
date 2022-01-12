---
title: "全てのカテゴリから検索"
draft: false
---
<input id = "query" onkeyup="location.replace('#' + this.value)" style="width: 90%;" autocomplete="off" autofocus placeholder="検索キーワードを入れてください" />

<div id = "result">
    <span id ="count">0</span> 件の質問・回答が見つかりました
</div>

<script>
    // 検索
    function search(query) {
        var count = 0;
        nquery = normalize(query);
        $(".card").each(function(i, elem) {
            var question = normalize($(elem).find("span").text());
            var answer = normalize($(elem).find(".card-body").text());
            if (nquery == "" || (question.indexOf(nquery) == -1 && answer.indexOf(nquery) == -1)) {
                $(elem).css("display", "none");
            } else {
                $(elem).css("display", "block");
                count++;
            }
        })
        $("#result #count").text(count);
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

    // 文字列を正規化する
    function normalize(str) {
        const alpha = normalizeAlphaNum(str);
        const kana = normalizeKana(alpha);
        const half = normalizeHalfKana(kana)
        return normalizeOthers(half);
    }
    // 英数字記号を半角化
    function normalizeAlphaNum(str) {
        return str.replace(/[！-～]/g, function(s) {
            return String.fromCharCode(s.charCodeAt(0) - 0xFEE0);
        }).toLowerCase();
    }
    // ひらがな→カタカナ
    function normalizeKana(str) {
        return str.replace(/[\u3041-\u3096]/g, function(s) {
            return String.fromCharCode(s.charCodeAt(0) + 0x60);
        });
    }
    // 半角カナ→全角カタカナ
    function normalizeHalfKana(str) {
        const convertMap = {
            'ｶﾞ': 'ガ', 'ｷﾞ': 'ギ', 'ｸﾞ': 'グ', 'ｹﾞ': 'ゲ', 'ｺﾞ': 'ゴ',
            'ｻﾞ': 'ザ', 'ｼﾞ': 'ジ', 'ｽﾞ': 'ズ', 'ｾﾞ': 'ゼ', 'ｿﾞ': 'ゾ',
            'ﾀﾞ': 'ダ', 'ﾁﾞ': 'ヂ', 'ﾂﾞ': 'ヅ', 'ﾃﾞ': 'デ', 'ﾄﾞ': 'ド',
            'ﾊﾞ': 'バ', 'ﾋﾞ': 'ビ', 'ﾌﾞ': 'ブ', 'ﾍﾞ': 'ベ', 'ﾎﾞ': 'ボ',
            'ﾊﾟ': 'パ', 'ﾋﾟ': 'ピ', 'ﾌﾟ': 'プ', 'ﾍﾟ': 'ペ', 'ﾎﾟ': 'ポ',
            'ｳﾞ': 'ヴ', 'ﾜﾞ': 'ヷ', 'ｦﾞ': 'ヺ',
            'ｱ': 'ア', 'ｲ': 'イ', 'ｳ': 'ウ', 'ｴ': 'エ', 'ｵ': 'オ',
            'ｶ': 'カ', 'ｷ': 'キ', 'ｸ': 'ク', 'ｹ': 'ケ', 'ｺ': 'コ',
            'ｻ': 'サ', 'ｼ': 'シ', 'ｽ': 'ス', 'ｾ': 'セ', 'ｿ': 'ソ',
            'ﾀ': 'タ', 'ﾁ': 'チ', 'ﾂ': 'ツ', 'ﾃ': 'テ', 'ﾄ': 'ト',
            'ﾅ': 'ナ', 'ﾆ': 'ニ', 'ﾇ': 'ヌ', 'ﾈ': 'ネ', 'ﾉ': 'ノ',
            'ﾊ': 'ハ', 'ﾋ': 'ヒ', 'ﾌ': 'フ', 'ﾍ': 'ヘ', 'ﾎ': 'ホ',
            'ﾏ': 'マ', 'ﾐ': 'ミ', 'ﾑ': 'ム', 'ﾒ': 'メ', 'ﾓ': 'モ',
            'ﾔ': 'ヤ', 'ﾕ': 'ユ', 'ﾖ': 'ヨ',
            'ﾗ': 'ラ', 'ﾘ': 'リ', 'ﾙ': 'ル', 'ﾚ': 'レ', 'ﾛ': 'ロ',
            'ﾜ': 'ワ', 'ｦ': 'ヲ', 'ﾝ': 'ン',
            'ｧ': 'ァ', 'ｨ': 'ィ', 'ｩ': 'ゥ', 'ｪ': 'ェ', 'ｫ': 'ォ',
            'ｯ': 'ッ', 'ｬ': 'ャ', 'ｭ': 'ュ', 'ｮ': 'ョ',
            '｡': '。', '､': '、', 'ｰ': 'ー', '｢': '「', '｣': '」', '･': '・'
        };
        return convert(str, convertMap);
    }
    // その他
    function normalizeOthers(str) {
        const convertMap = {
            '一回': '1回', '二回': '2回', '三回': '3回', '四回': '4回', '五回': '5回',
            '六回': '6回', '七回': '7回', '八回': '8回', '九回': '9回', '十回': '10回',
            'スマホ': 'スマートフォン', 'スマフォ': 'スマートフォン', 'アプリケーション': 'アプリ', 
            '2次元': '二次元', '個人番号': 'マイナンバー', '市町村': '市区町村',
            '摂取': '接種', '接収': '接種', '何時': 'いつ', '何処': 'どこ'
        };
        return convert(str, convertMap);
    }
    // Map 変換
    function convert(str, convertMap) {
        const reg = new RegExp('(' + Object.keys(convertMap).join('|') + ')', 'g');
        return str.replace(reg, function(s) {
            return convertMap[s];
        }).replace(/ﾞ/g, '゛').replace(/ﾟ/g, '゜');
    }
</script>

{{< result >}}
