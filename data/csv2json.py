import csv
import json
import random


def csv_to_json(dataset_name, csv_file_path):
    """
    将 CSV 文件转换为训练集和评估集的 JSON 文件。

    :param dataset_name: 数据集名称（用于生成文件名）
    :param csv_file_path: 输入的 CSV 文件路径
    """
    # 创建一个空列表存储数据
    data = []

    # 读取 CSV 文件并将其转换为字典列表
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # 自动将每行转换为字典
        headers = next(csv_reader)
        for row in csv_reader:
            data.append(row['processed_title'])  # 将每行数据添加到列表中
            # if len(data) == 11000:
            #     break

    # Shuffle
    random.shuffle(data)

    # S1
    s1_data = data[:10000]
    # 训练集：整个数据集
    train_data = data[10000:15000]

    # 评估集：整个数据集，封装为 {"1": [list of samples]}
    eval_data = {"1": data[15000:]}

    # 保存 S1 到 [dataset_name]_s1.json
    with open(f"initialization.json", "w", encoding="utf-8") as s1_file:
        json.dump(s1_data, s1_file, indent=4, ensure_ascii=False)
        print(f"S1 已保存到 initialization.json")

    # 保存训练集到 [dataset_name]_train.json
    with open(f"{dataset_name}_train.json", "w", encoding="utf-8") as train_file:
        json.dump(train_data, train_file, indent=4, ensure_ascii=False)
        print(f"训练集已保存到 {dataset_name}_train.json")


    # 保存评估集到 [dataset_name]_eval.json
    with open(f"{dataset_name}_eval.json", "w", encoding="utf-8") as eval_file:
        json.dump(eval_data, eval_file, indent=4, ensure_ascii=False)
        print(f"评估集已保存到 {dataset_name}_eval.json")

    print(len(s1_data))
    print(len(train_data))
    print(len(eval_data["1"]))

# 示例调用
if __name__ == "__main__":
    # 数据集名称
    dataset_name = "haiku"

    # CSV 文件路径
    csv_file_path = "haiku.csv"

    # 调用函数
    csv_to_json(dataset_name, csv_file_path)
