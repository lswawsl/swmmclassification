# model settings
model = dict(
    type='ImageClassifier',
    # 提特征
    backbone=dict(
        type='ResNet',
        depth=18,
        num_stages=4,
        out_indices=(3, ), #选择哪个stage的作为输出
        style='pytorch'),
    # 全局平均池化 对特征进行融合
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=512,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5), # top评估标准
    ))
