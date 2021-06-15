import json

def make_pair_data(fname):
    """
        入力：ファイル名
        出力：ユーザ-システム対話ペア (us_src: list, us_tar: list)
        　　　システム-ユーザ対話ペア (su_src: list, su_tar: list)
    """
    # 適切な対話かどうかの閾値[0,1]、高いほど厳しい(default:0.5)
    threshold = .5
    # src: User, tar: System
    # 対話破綻ではないと考えられる応答をしている場合のみデータに含める
    us_src = []
    us_tar = []
    # src: System, tar: User
    # システムの発話に対して人間が応答しているため正しい応答とし、すべての文を対話データに含める
    # （文脈を考慮してないため少し暴論）
    su_src = []
    su_tar = []
    with open(fname, 'rb') as f:
        data = json.load(f)
    pre_user_uttr = ''
    pre_sys_uttr = ''
    for turn in data['turns']:
        # システムが応答時
        if turn['speaker'] == 'S':
            pre_sys_uttr = turn['utterance']
            if not pre_user_uttr:
                continue
            ann_list = []
            for ann in turn['annotations']:
                ann_list.append(ann['breakdown'])
            # 対話破綻ではないと判定している人が半数以上であればデータに含める
            if ann_list.count('O') / len(ann_list) > threshold:
                us_src.append(pre_user_uttr)
                us_tar.append(turn['utterance'])
            pre_sys_uttr = turn['utterance']
        # ユーザが応答時
        elif turn['speaker'] == 'U':
            pre_user_uttr = turn['utterance']
            if not pre_sys_uttr:
                continue
            su_src.append(pre_sys_uttr)
            su_tar.append(turn['utterance'])

    assert len(us_src) == len(us_tar)
    assert len(su_src) == len(su_tar)

    return (us_src, us_tar), (su_src, su_tar)

def write_data(file_list, output_dir):
    # 各ファイルからpair dataを取ってくる
    us_src = []
    us_tar = []
    su_src = []
    su_tar = []
    for fname in file_list:
        (us_x, us_y), (su_x, su_y) = make_pair_data(fname)
        us_src += us_x
        us_tar += us_y
        su_src += su_x
        su_tar += su_y
    src = us_src+su_src
    tar = us_tar+su_tar

    assert len(src) == len(tar)
    # 書き込み
    print('source: 文数', len(src))
    with open(output_dir + 'source.txt', 'w') as f:
        for s in src:
            f.write(s + '\n')
    print('source: finished.')
    print('target: 文数', len(tar))
    print('target: writing...')
    with open(output_dir + 'target.txt', 'w') as f:
        for t in tar:
            f.write(t + '\n')
    print('target: finished.')