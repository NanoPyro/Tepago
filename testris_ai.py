import random

class TetrisAI():
    def __init__(self):
        self.weights = [
            self.get_weight_setting("gross_heights", 0.3, 0.1),
            self.get_weight_setting("hole_count", 0.3, 0.1),
            self.get_weight_setting("block_count", 0.3, 0.1),
            self.get_weight_setting("block_floor", 0.3, 0.1),
            self.get_weight_setting("line_clear", 0.3, 0.1),
            self.get_weight_setting("height_std", 0.3, 0.1),
            self.get_weight_setting("height_difference", 0.3, 0.1),
        ]
        self.mutation_mu = 0.0
        self.mutation_sigma = 1.0
        self.chromosomes = []
        

    def get_weight_setting(self, name, mutation_boundary, mutation_chance):
        return {
            "name": name,
            "mutation_boundary":mutation_boundary,
            "mutation_chance":mutation_chance
        }
    
    def ga_init(self, count):
        if count%2 != 0:
            raise Exception("count is not even number")
        self.chromosomes = [self.get_random_weight() for _ in range(count)]
    
    # 한 판 학습한다.
    def study(self, kibo):
        
        # choice 함수를 실행하면서 나온 결과값을 테트리스 라이브러리에서 기보에 저장해둔다.
        # 그 결과값을 총합한다.
        # 염색체끼리 총합한 결과값으로 비교해서 선택한다.
        
        pass

    def choice(self, arrary):
        arrary = [{
            # 블록을 내리기 전의 맵
            # 블록을 내린 후의 맵
            # 몇 칸을 부쉈는지
            # 마지막 줄에 두었는지
        }, {
            # 블록을 내리기 전의 맵
            # 블록을 내린 후의 맵
            # 몇 칸을 부쉈는지
            # 마지막 줄에 두었는지
        }]

        # 가장 적당한 선택과 함께 점수를 반환한다.
        pass

    def get_random_weight(self):
        return [random.random() for _ in self.weights]

    def ga_select(self, count):
        return sorted(self.chromosomes)[-count:]

    def ga_crossover(self, count):
        origin_chrom_count = self.chromosomes.__len__()
        if count > origin_chrom_count / 2:
            raise Exception("too much count")
        
        temp_chrom = self.chromosomes.copy()

        for _ in range(count):
            chrom_count = temp_chrom.__len__()

            # 무작위로 두 염색체 선택, 무작위로 교환할 유전자 선택, 유전자 교환
            i = random.randrange(chrom_count)
            j = random.randrange(chrom_count)
            pick_gene = random.randrange(len(self.weights))
            while(True):
                if i == j:
                    j = random.randrange(chrom_count)
                else:
                    break

            chromo_A = self.chromosomes[i]
            chromo_B = self.chromosomes[j]
            
            chromo_A[pick_gene], chromo_B[pick_gene] = chromo_B[pick_gene], chromo_A[pick_gene]
            
            del temp_chrom[i]
            del temp_chrom[j]

                

    def ga_mutation(self):

        for chrom in self.chromosomes:
            for i, weight in enumerate(self.weights):
                # weight = self.weights[weight_name]
                mutation_boundary = weight["mutation_boundary"]
                mutation_chance = weight["mutation_chance"]
                
                if random.random() > mutation_chance:
                    continue
                
                chrom[i] += self.get_random_gauss(mutation_boundary)


    def get_random_gauss(self, boundary):

        gauss_values = [random.gauss(0, 1) for _ in range(1000)]

        gauss_values = [value for value in gauss_values if value >= 0]
        gauss_values.sort()

        gauss_min = gauss_values[0]
        gauss_max = gauss_values[-1]
        rate = boundary / (gauss_max - gauss_min)

        value = random.choice(gauss_values) * rate

        if bool(random.getrandbits(1)):
            value = -value
        return value


    
        


# [0] : 각 열의 높이들의 합
# [1] : 구멍 갯수
# [2] : 블록 갯수
# [3] : 블록을 바닥에 닿게 해서 얻은 점수
# [4] : 라인 제거로 얻은 점수
# [5] : 높이의 표준편차
# [6] : 최대 높이와 최소 높이의 차이


# 1. 처음에 가중치를 정한다.
# 2. 유전자를 랜덤으로 n개 생성한다
# 3. 각 유전자마다 가중치와 아이디를 가지고 있는데 여기에서 가중치는 랜덤으로 설정한다.
# 4. 테트리스를 플레이한다. (n번)
# 5. 유전자들에게 테트리스를 플레이하면서 얻은 점수들로 순위를 매긴다.
# 6. 점수가 높은 유전자를 x개 선택한다.
# 7. 유전자끼리 랜덤으로 교차한다. (교차할 유전자 개수는 변수로 설정한다.)
# 8. 각 가중치에 설정된 비율에 따라 변이를 한다. (이 방식이 아니어도 어쨋든 변이한다.)
# 9. 후대 유전자를 선택된 유전자로 교체한다.
# 10. 4번부터 9번까지 반복하면서 세대를 교체해나간다.


TetrisAI()