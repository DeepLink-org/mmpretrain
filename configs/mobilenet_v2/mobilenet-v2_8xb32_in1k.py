_base_ = [
    '../_base_/models/mobilenet_v2_1x.py',
    '../_base_/datasets/mobilenetv2_imagenet_bs32_pil_resize.py.py',
    '../_base_/schedules/imagenet_bs256_epochstep.py',
    '../_base_/default_runtime.py'
]
