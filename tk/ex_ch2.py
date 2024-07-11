from bs4 import BeautifulSoup
from translate import Translator

def translate_text_translate_lib(text, src='zh', dest='en'):
    translator = Translator(from_lang=src, to_lang=dest)
    translation = translator.translate(text)
    return translation

def extract_and_translate(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract all text from <p> tags
    paragraphs = soup.find_all('p')
    original_texts = [p.get_text() for p in paragraphs]
    concatenated_text = "\n".join(original_texts)

    # Split text into chunks if necessary to avoid length issues
    max_chunk_size = 5000  # Define a maximum chunk size for translation
    chunks = [concatenated_text[i:i + max_chunk_size] for i in range(0, len(concatenated_text), max_chunk_size)]

    # Translate each chunk
    translated_chunks = [translate_text_translate_lib(chunk) for chunk in chunks]

    # Join translated chunks back into a single string
    translated_text = "\n".join(translated_chunks)

    # Split the translated text back into individual paragraphs
    translated_texts = translated_text.split('\n')

    # Replace the original text in <p> tags with the translated text
    for i, p in enumerate(paragraphs):
        if i < len(translated_texts):
            p.string = translated_texts[i]
        else:
            p.string = ''

    # Get the modified HTML
    modified_html = str(soup)
    return modified_html

html_content = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<h1>
 <span class="title">
  第一百九十章、跑偏了
 </span>
</h1>
<div class="rp-article bookContent" id="bookContent">
 <p>
  “哈德逊，这次拍卖会，你要过去么？”
 </p>
 <p>
  梅丽莎跃跃欲试的问道。
 </p>
 <p>
  “凯姆伯尹大师”，对所有的魔法师来说，都是神一般的存在。他的实验室被发现，必定会吸引无数目光。
 </p>
 <p>
  作为一名魔法师，梅丽莎也不能例外。看那热切的表情分明是在说：带她一起去。
 </p>
 <p>
  在一起生活了几年，这点儿判断力，哈德逊还是有的。可惜莫西人抛出来的实验室，不一定是真的啊！
 </p>
 <p>
  正常情况下，发现这种东西，大家都恨不得藏的严严实实，谁会公开讯息啊？
 </p>
 <p>
  就算不怕贼偷，也怕贼惦记啊！
 </p>
 <p>
  当然，造假也不会太过分。根据莫西人前面几次宝藏发掘的情况来看，实验室肯定是凯姆伯尹大师使用过的，是不是刚刚才发现的，那就很难说了。
 </p>
 <p>
  作为一名顶尖强者，凯姆伯尹当年游历大陆，在很多地方都留下过足迹。
 </p>
 <p>
  只是后来突然神秘失踪，并没有留下系统性的传承。包括他的学生，都没有能够完全继承凯姆伯尹大师的研究成果。
 </p>
 <p>
  “去，必须去！
 </p>
 <p>
  刚被发现的凯姆伯尹大师实验室，应该保持住了原来的模样，作为一名魔法师，怎么能不去参观一番呢？
 </p>
 <p>
  在家闲着，也没什么事。梅丽莎，你也跟着一起去逛逛吧！”
 </p>
 <p>
  哈德逊笑呵呵的说道。
 </p>
</div>
</html>
"""

translated_html = extract_and_translate(html_content)
print(translated_html)

with open('translated_chapter.html', 'w', encoding='utf-8') as file:
    file.write(translated_html)