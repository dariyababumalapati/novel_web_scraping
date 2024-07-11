from deep_translator import GoogleTranslator
import time

def translate_text(text, src='zh-CN', dest='en'):
    translator = GoogleTranslator(source=src, target=dest)
    for attempt in range(5):  # Retry up to 5 times
        try:
            translation = translator.translate(text)
            return translation
        except Exception as e:
            print(f"Attempt {attempt + 1} failed. Error: {e}. Retrying...")
            time.sleep(2)  # Wait for 2 seconds before retrying

    raise Exception("Translation failed after multiple attempts.")


chinese_text = """另立教廷风波还在持续但哈德逊已经不担心了教廷没有第一时间动手那就意味着要采取外交手段解决问题很明显这是被逼出来的结果没有各国的支持劳师远征法兰克王国教廷完全没有任何胜算想要杀鸡儆猴都找不到合适 的目标直接反教廷的都不好惹大陆上的异端份子那么多万一不小心损失惨重那才是真的要完蛋中立反教廷的略微要好欺负一些但政治影响 太过恶劣搞不好鸡没有杀死反而将中立派系的逼到了直接反教廷阵营让局势变得更加恶劣既得利益者们又不傻自然要权衡利弊考虑到的问 题越多就越不敢动手见双方打起了嘴炮哈德逊也就放心了短时间内不打起来就行后续谁也没有奢望两大霸主能够和平相处真要是法兰克王 国和教廷和解阿尔法王国也就没法混了以往的时候王国敢和教廷对着干除了双方距离远外最重要的就是有法兰克人在前面顶着最近这些年 只要教廷搞大行动法兰克王国必定会拖后腿反之也是亦然两家大势力互相添堵各国才有好日子过放下手中的情报后哈德逊继续和幕僚们完 善雪月领开发计划公爵按照王国的近东战略规划我们将是第一批开荒者综合各方面因素之后政务部认为领地的前期开发以港口为核心即可 兽人缺乏航海技术就算是发生变故我们也可以从海上撤离首批移民主要以渔民为主既可解决前线驻军的肉食问题又可以免受兽人的威胁政 务部计划港口开辟成功之后先向新月港输送三千渔民待站稳脚跟后再逐步增加移民数量从港口开辟进度来看移民工作将在明年展开预计神 圣历年我们将向雪月领移民两万人三年之后在当地的移民总数将突破十万雅各布意气风发的说道这次东进开发雪月领他们都是受益者哈德 逊的画饼技术虽然很初级但在亚斯兰特大陆绝对是跨时代的为了让手下人卖力干活哈德逊老爷已经为大家描绘了雪月领开发完成后的美好 画卷身份地位荣华富贵那是应有尽有出于防备兽人的目的哈德逊甚至还创造了独具特色的新贵族体系封地爵位自然是有的只不过大家不需 要单独去管理而是他这个封君统一进行规划管理大家直接拿收益分红即可正常情况下这么玩儿肯定会被人认为这是图谋不轨但是近东地区 例外有兽人那个好邻居在中小贵族的领地能够收支平衡都是一个奇迹稍有不慎就是身死领地灭与其每天生活在危机之中"""

translated_text = translate_text(chinese_text)
print(translated_text)

# Read the text from the file
with open('chin.txt', 'r', encoding='utf-8') as f:
    chinese_text = f.read()

# Strip any extraneous whitespace
chinese_text = chinese_text.strip()

# Print the Chinese text to ensure it is read correctly
print("Chinese Text:", chinese_text)

# Translate the text
translated_text = translate_text(chinese_text)

# Print the translated text
print("Translated Text:", translated_text)
