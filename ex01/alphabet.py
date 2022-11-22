import random
import datetime

qa_lst = []
while len(qa_lst) !=10:
    qa_lst.append(chr(random.randint(65,90)))
    qa_lst = list(set(qa_lst))
qa_lst_copy = qa_lst.copy()
ans_lst = [qa_lst.pop(random.randint(0,len(qa_lst)-1))for i in range(2)]
random.shuffle(qa_lst)

def shutudai(qa_list_copy,qa_list,ans_list):
    print("対象文字")
    for i in qa_list_copy:
        print(i,end=" ")
    """
    print("\n欠損文字")
    for i in ans_list:
        print(i,end=" ")
    """
    print("\n表示文字")
    for i in qa_list:
        print(i,end=" ")
    return ans_list


def kaitou(ans_list):
    a = 0
    st = datetime.datetime.now()
    for i in range(1,6):
        if a==0:
            ans_f = input("\n欠損文字はいくつになるでしょうか?：")
            if len(ans_list) == int(ans_f):
                print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
                a+=1
            else:
                ("不正解です")
                pass

        else:
            if len(ans_list) != 0:
                ans_s = input(f"{a}つ目の文字を入力してください：")
                if ans_s in ans_list:
                    a +=1
                    ans_list.remove(str(ans_s))
                else:
                    ("不正解です")
                    pass
            else:
                ed = datetime.datetime.now()
                print("正解です。全て解答できたため終了いたします")
                print(f"解答時間は{(ed-st).seconds}秒でした")
                break
    else:
        print("不正解です。5回以上間違えたため終了いたします\nまた挑戦してください")

def main(qa_lst_copy,qa_lst,ans_lst):
    ans = shutudai(qa_lst_copy,qa_lst,ans_lst)
    kaitou(ans)

if __name__ == "__main__":
    main(qa_lst_copy,qa_lst,ans_lst)
