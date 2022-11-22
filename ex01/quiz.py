import random
import datetime

def shutdai(qa_lst):
    quetion,ans = random.choice(list(qa_lst.items()))
    print(f"問題:\n{quetion}")
    return ans

def kaitou(ans):
    st = datetime.datetime.now()
    ans_input = input("答えよ：")
    ed = datetime.datetime.now()
    if ans_input in ans:
        return f"{(ed-st).seconds}秒かかっているが正解だ"
    else:
        return "出直してこい"

def main(quetsiton_ans):
    ans = shutdai(quetsiton_ans)
    print(kaitou(ans))


if __name__ == "__main__":
    qa_lst = {"サザエの旦那の名前は？":("マスオ", "ますお"),
                "カツオの妹の名前は？":("ワカメ", "わかめ"),
                "タラオはカツオから見てどんな関係？":("甥", "おい", "甥っ子", "おいっこ")}
    main(qa_lst)
