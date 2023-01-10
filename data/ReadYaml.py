
import os.path
import yaml

file_path = os.path.join(os.path.dirname(__file__), 'login_data.yaml')

def read_yaml(key,key1):
    with open(file_path) as f:
        result = yaml.load(f, yaml.FullLoader)
        if key in result.keys():
            return result[key][key1]
        else:
            raise Exception('key不在当前yaml内')


if __name__ == '__main__':
    print(read_yaml('loginPage', 'password_element'))