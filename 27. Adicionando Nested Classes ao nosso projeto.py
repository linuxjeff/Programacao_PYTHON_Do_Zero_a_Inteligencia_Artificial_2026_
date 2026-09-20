# criar a classe Man=in

class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock):
        self.modelo = modelo
        self.gpu_nome = gpu_nome
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)

    def mostrar_configuracao(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu()
        self.cpu.mostar_cpu()


    class GPU:
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f'GPU: {self.nome} - VRAM: {self.memoria_gb}MB')


    class CPU:
        def __init__(self, nome, cores, clock_gh):
            self.nome = nome
            self.cores = cores
            self.clock_gh = clock_gh

        def mostar_cpu(self):
            print(f'CPU: {self.nome} - CPU Cores: {self.cores} - CPU Clock GH: {self.clock_gh}')


pc1 = Computador('Dell', '460', 24, 'I5', 4, 2.5)
pc1.mostrar_configuracao()