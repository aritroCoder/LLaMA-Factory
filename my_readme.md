## Train
CUDA_VISIBLE_DEVICES=4 llamafactory-cli train examples/train_qlora/llama3_lora_sft_bnb_npu.yaml

## Inference server
API_PORT=8000 CUDA_VISIBLE_DEVICES=4 llamafactory-cli api examples/inference/llama3_lora_sft.yaml

## Inference client
python run_model.py