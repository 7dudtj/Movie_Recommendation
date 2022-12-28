# RecBole

RecVAE ���� ����ϱ� ���Ͽ� RecBole�� �����Ͽ�����, ���� �ٸ� �𵨷� ��� ������ ���� �� �ֽ��ϴ�.  

# Directory Structure

config - �� �� config ������ �����մϴ�. ������ Ȯ���ڴ� .yaml �Դϴ�.  
data - RecBole���� ����ϴ� data �����Դϴ�. ������ movie ������ ������, �̰��� �����Ͱ� ����˴ϴ�.  
model - �н��� ���� ����˴ϴ�.  

# Files

data_creator.py - submission�� �ʿ��� unique_user.csv ���ϰ� RecBole�� ���Ǵ� Atomic Files (ex. .inter, .item, .user ...)�� �����մϴ�.  
hyper.test - hyper parameter tuning�� ���Ǵ� �����Դϴ�. Tuning �ϰ��� �ϴ� parameter�� �����մϴ�.  
inference.py - Movie Recommendation ��ȸ�� �µ��� ���� inference�ϸ�, submission.csv ������ �����մϴ�.  
requirements.txt - ```pip install -r requirements.txt``` ��ɾ ���� ��ġ�� �� �ֽ��ϴ�.  
run_hyper.py - hyper parameter tuning�� �ϴ� �����Դϴ�.  
train.py - �� �н��� �ϴ� �����Դϴ�.  
utils.py - submission ���ۿ� �ʿ��� ���� �Լ����� �ֽ��ϴ�.  

# How to run

0. data/train ���丮�� new_years.tsv ������ �־���մϴ�. ���� ���, EDA/YYS_EDA_Year.ipynb�� �����Ͽ� ������ �� �ֽ��ϴ�.
1. �н��ϰ��� �ϴ� �𵨿� ���� .yaml ������ RecBole/config�� �־�� �մϴ�. ���� RecVAE.yaml�� �����մϴ�.
2. �Ϻ� ���� ���, Trainer�� �������� ��������� �մϴ�. �ڼ��� ������ [RecBole Docs](https://recbole.io/docs/recbole/recbole.trainer.trainer.html#module-recbole.trainer.trainer) ���� Ȯ�� �ٶ��ϴ�.
3. requirements�� ��ġ�Ͽ��� ȯ���� �����ݴϴ�.
4. ```python data_creator.py``` ��ɾ �Է��Ͽ� RecBole�� �ʿ��� �����͸� �����մϴ�.
5. ```python train.py --model=[�𵨸�] --config_files=[�𵨸�.yaml]``` ��ɾ �Է��Ͽ� �н��� �����մϴ�.
6. ```python inference.py --config_files=[�𵨸�.yaml] --type=[���� type]``` ��ɾ �Է��Ͽ� �߷��� �����մϴ�.
7. ���� ������ code/submission�� ����˴ϴ�.

# More information

���� �迭�� ���� �ʿ��� input ������ ������ �ٸ��ϴ�. �ڼ��� ������ [��ũ](https://recbole.io/docs/user_guide/data/atomic_files.html) ���� Ȯ���� �� �ֽ��ϴ�.  
�̹� ��ȸ�� �ַ� ���� General �迭�̳� Sequential �迭�� ��� .inter ���ϸ��� �ʼ������� �䱸�մϴ�.