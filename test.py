import utils

config = utils.load_yaml('modules/auto_correct/config.yaml')
correcter = utils.create_instance(config['auto_correct'])

print(correcter('TRUNG TÂM KIỂM NGHIỆM'))