from modulos import *

class Relatorios():
    def printaluno(self):
        webbrowser.open("aluno.pdf")
    def geraRelataluno(self):
        self.c = canvas.Canvas("aluno.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.fone_entry.get()
        self.cepRel = self.cep_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        self.enderecoRel = self.lograd_entry.get()
        self.bairroRel = self.bairro_entry.get()
        self.ad1Rel = self.ad1_entry.get()
        self.ad2Rel = self.ad2_entry.get()
        self.adfRel = self.adf_entry.get()


        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do aluno')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Codigo: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ')
        self.c.drawString(50, 600, 'CEP: ')
        self.c.drawString(50, 570, 'Cidade: ')
        self.c.drawString(50, 540, 'Endereço: ')
        self.c.drawString(50, 510, 'Bairro: ')
        self.c.drawString(50, 480, 'AD1: ')
        self.c.drawString(50, 450, 'AD2: ')
        self.c.drawString(50, 420, 'Nota Final: ')
        self.c.drawString(50, 390, 'Falculdade:')
        self.c.drawString(50, 360, 'Curso: ')
        

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 630, self.foneRel)
        self.c.drawString(150, 600, self.cepRel)
        self.c.drawString(150, 570, self.cidadeRel)
        self.c.drawString(150, 540, self.enderecoRel)
        self.c.drawString(150, 510, self.bairroRel)
        self.c.drawString(150, 480, self.ad1Rel)
        self.c.drawString(150, 450, self.ad2Rel)
        self.c.drawString(150, 420, self.adfRel)
        self.c.drawString(150, 390, 'FADAM')
        self.c.drawString(150, 360, 'Análise e Desenvolvimento de Sistemas ')
        
        
        self.c.rect(20, 720, 550, 200, fill= False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printaluno()