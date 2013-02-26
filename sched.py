class Processo:
  id = 1

  def __init__(self, duracao):
    self.id = Processo.id
    Processo.id += 1
    self.duracao = duracao
    
  def __repr__(self):
    return "Processo (" + str(self.id) + ")"
    
class Processador:
  id = 1
  
  def __init__(self):
    self.id = Processador.id
    Processador.id += 1
    self.processos = []
    self.processo_atual = None
  
  def __repr__(self):
    return "Processador (" + str(self.id) + ") -> " + str(self.processos)
    
  def em_execucao(self):
    return self.processo_atual != None
    
  def agendar(self, p):
    self.processos.append(p)
    self.processo_atual = p
    
  def executar(self, t):
    if (self.em_execucao()):
      self.processo_atual.duracao -= t
      
  def remover_processo(self):
    if (self.em_execucao() and self.processo_atual.duracao == 0):
      self.processo_atual = None
      
    return self
    
def tempo_processo_atual(processador):
  if (processador.processo_atual == None):
    return max_int
  else:
    return processador.processo_atual.duracao

def executar_processo_por_tempo(t):
  def closure(p):
    p.executar(t)
    return p
    
  return closure  

def alocar_processos(p):
  if (len(processos)):
    if (not p.em_execucao()):
      p.agendar(processos.pop(0))
      
  return p

processos = []
processadores = []

total_processadores = input()
for p in range(total_processadores):
  processadores.append(Processador())
  
max_int = -1
total_processos = input()
for p in range(total_processos):
  duracao = input()
  processos.append(Processo(duracao))
  if (duracao > max_int):
    max_int = duracao

max_int += 1
relogio = 0

#alocando processos
processadores = map(alocar_processos, processadores)
    
while len(processos):
  #descobrindo o proximo processo que vai terminar
  processador = min(processadores, key=tempo_processo_atual)

  #quanto tempo levou ate o final
  tempo_minimo = processador.processo_atual.duracao

  #atualizando o relogio global
  relogio += tempo_minimo

  #atualizando tempo execucao de todos os processadores
  processadores = map(executar_processo_por_tempo(tempo_minimo), processadores)

  #removendo os processos completos
  processadores = map(lambda p: p.remover_processo(), processadores)
     
  #alocando processos
  processadores = map(alocar_processos, processadores)

#terminando todos os processos
processador = max(filter(lambda p: len(p.processos) > 0, processadores), key=tempo_processo_atual)

relogio += processador.processo_atual.duracao

print "### Fim do escalonamento ###"
print "Tempo total de execucao: ", relogio, " u.t."
for p in processadores:
  print p
