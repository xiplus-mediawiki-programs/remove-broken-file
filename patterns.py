# -*- coding: utf-8 -*-
REGEX = [
    # infobox
    {
        'pattern': r'(\|\s*)((?:\d+|image[ _-]?(?:|\d+|file[LR]?\d*|flag|map|name|seal|shield|skyline|coat|coat[ _]of[ _]arms|blank[ _]emblem|hans|hant|cn|hk|mo|sg|tw)?|img_\d+|(?:map|dual|net|vfig|uniform|ship|logo|kit|stdg|hans|hant|cn|hk|mo|sg|tw)[ _-]?image|logo[ _-]?(?:file|filename|pic)?|(?:company|uniform)[ _-]?logo|photo\d*[a-c]?|coa[ _-]pic|img|filename|chart|screenshot|cover|symbol|audio[ _-]file|signature|album|(?:city)?[ _-]?seal|map[ _-]?(?:img|location)?|(?:range|Alternative)[ _-]?map|patch|badge|coatofarms|session[ _-]room|static[ _-]image[ _-]name|mapofstate|ribbon|uniform|insignia|zh-?(?:hans|hant|cn|hk|mo|sg|tw)?|flag_[sp]\d+|flag alias[A-Za-z\- ]*|BILDPFAD_KARTE|(?:代表)?(?:圖片|图片|圖像|图像|画像)(?:名称|名稱|\d+)?|電視網商標檔案|[頻频]道[圖图]片(?:檔案|文件)|電臺圖片檔案|路線圖|正面|背面|项目符号文件名称|地图档名|簽名|签名|照片|市旗|市徽|景观照片文件名|画像ファイル)\s*=\s*(?:<!--[^\n]+-->)?\s*)((?:File|Image|文件|檔案|圖像):)? *({0})(?:#.+?)?(\s*?(?:<!--[^\n]+-->)?\s*?(?:\||}}|\n))',
        'replace': {
            'comment_other': r'\1\2<!-- 檔案不存在 \3\4 ，可從{0}取得 -->\5',
            'moved': r'\1\2\g<3>{0}\5',
            'deleted_comment': r'\1\2<!-- 檔案已被刪除 \3\4 -->\5',
            'deleted': r'\1\2\5',
            'comment': r'\1\2<!-- 檔案不存在 \3\4 -->\5'
        }
    },
    # normal_whole_line
    {
        'pattern': r'(^|\n)[ \t]*(\[\[(?:File|Image|文件|檔案|圖像):) *({0})(?:#.+?)?(\s*(?:\|(?:\[\[[^[\]]*\]\]|\[[^[\]]*\]|[^[\]])*)?\]\])[ \t]*(\n|$)',
        'replace': {
            'comment_other': r'\1<!-- 檔案不存在 \2\3\4 ，可從{0}取得 -->\5',
            'moved': r'\1\g<2>{0}\4\5',
            'deleted_comment': r'\1<!-- 檔案已被刪除 \2\3\4 -->\5',
            'deleted': r'\1',
            'comment': r'\1<!-- 檔案不存在 \2\3\4 -->\5'
        }
    },
    # normal
    {
        'pattern': r'(\[\[(?:File|Image|文件|檔案|圖像):) *({0})(?:#.+?)?(\s*(?:\|(?:\[\[[^[\]]*\]\]|[^[\]])*)?\]\])([ \t]*)',
        'replace': {
            'comment_other': r'<!-- 檔案不存在 \1\2\3 ，可從{0}取得 -->',
            'moved': r'\g<1>{0}\3\4',
            'deleted_comment': r'<!-- 檔案已被刪除 \1\2\3 -->',
            'deleted': r'',
            'comment': r'<!-- 檔案不存在 \1\2\3 -->'
        }
    },
    # gallery
    {
        'pattern': r'(<gallery[^>\n]*?>[\s\S]*?\n)((?:File|Image|文件|檔案|圖像):)? *({0})(?:#.+?)?([ \t]*)(\|[^\n]*?)?\n([\s\S]*?</gallery>)',
        'replace': {
            'comment_other': r'\1<!-- 檔案不存在 \2\3\4\5 ，可從{0}取得 -->\n\6',
            'moved': r'\1\g<2>{0}\4\5\n\6',
            'deleted_comment': r'\1<!-- 檔案已被刪除 \2\3\4\5 -->\n\6',
            'deleted': r'\1\6',
            'comment': r'\1<!-- 檔案不存在 \2\3\4\5 -->\n\6'
        }
    },
    # Flagicon image
    {
        'pattern': r'({{{{(?:flagicon image|Wide image|Spoken Wikipedia)\|)({0})(?:#.+?)?((?:\|[^{{}}]*?)?}}}})([ \t]*)',
        'replace': {
            'comment_other': r'<!-- 檔案不存在 \1\2\3 ，可從{0}取得 -->',
            'moved': r'\g<1>{0}\3\4',
            'deleted_comment': r'<!-- 檔案已被刪除 \1\2\3 -->',
            'deleted': r'',
            'comment': r'<!-- 檔案不存在 \1\2\3 -->'
        }
    }
]
