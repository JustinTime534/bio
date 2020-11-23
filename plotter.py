import csv
import numpy as np
import matplotlib.pyplot as plt
fichiers=[]
for num in range(10):
    nomFichier = "path\\to\\file\\gen{}.csv".format(num+1)
    fichiers.append(nomFichier)
    print("done {}".format(num))

part_fig_homorec, part_ax_homorec = plt.subplots(subplot_kw=dict(ylim=(0,50*1.05)))
part_ax_homorec.set_title("population de lapins homozygotes récessifs sur 10 générations\nsimulé 1 000 000 de fois")
part_ax_homorec.set_ylabel("population de lapins homozygotes récessifs")
part_ax_homorec.set_xlabel("numéro de la génération")
part_ax_homorec.set_xticks(np.arange(1,11,1))
part_ax_homorec.set_axisbelow(True)
part_ax_homorec.minorticks_on()
part_ax_homorec.grid(which="minor",linestyle=":",linewidth="0.25",color="blue")
part_ax_homorec.grid(which="major",linestyle="-",linewidth="0.5",color="black")

part_fig_hetero, part_ax_hetero = plt.subplots(subplot_kw=dict(ylim=(0,50*1.05)))
part_ax_hetero.set_title("population hétérozygote")
part_ax_hetero.set_xticks(np.arange(1,11,1))
part_ax_hetero.set_axisbelow(True)
part_ax_hetero.minorticks_on()
part_ax_hetero.grid(which="minor",linestyle=":",linewidth="0.25",color="blue")
part_ax_hetero.grid(which="major",linestyle="-",linewidth="0.5",color="black")

part_fig_homodom, part_ax_homodom = plt.subplots(subplot_kw=dict(ylim=(0,50*1.05)))
part_ax_homodom.set_title("population homozygote dominante")
part_ax_homodom.set_xticks(np.arange(1,11,1))
part_ax_homodom.set_axisbelow(True)
part_ax_homodom.minorticks_on()
part_ax_homodom.grid(which="minor",linestyle=":",linewidth="0.25",color="blue")
part_ax_homodom.grid(which="major",linestyle="-",linewidth="0.5",color="black")

part_fig_gen, part_ax_gen = plt.subplots(subplot_kw=dict(ylim=(0,50*1.05)))
part_ax_gen.set_title("population generale de lapins, comparaison entre\
        \nhomozygotes récessifs, hétérozygotes, homozygotes dominants\
        \nsimulé 1 000 000 de fois")
part_ax_gen.set_xlabel("numéro de la génération")
part_ax_gen.set_ylabel("population d'un type spécifique de lapins")
part_ax_gen.set_xticks(np.arange(1,11,1))
part_ax_gen.set_axisbelow(True)
part_ax_gen.minorticks_on()
part_ax_gen.grid(which="minor",linestyle=":",linewidth="0.25",color="blue")
part_ax_gen.grid(which="major",linestyle="-",linewidth="0.5",color="black")

for i in range(10):
    with open(fichiers[i],"r") as rf:
        reader = csv.reader(rf, delimiter=",")
        for row in reader:
            #part_ax_homorec.plot(i+1,int(row[1]), marker='o', markersize=1.5,color = "red")
            #part_ax_hetero.plot(i,decomptes[i][1], marker='o', markersize=1.5,color = "green")
            #part_ax_homodom.plot(i,decomptes[i][2], marker='o', markersize=1.5,color = "blue")
            part_ax_gen.plot(i+0.7,int(row[1]), marker='o', markersize=1.5,color = "red", label="ff")
            part_ax_gen.plot(i+0.8,int(row[2]), marker='o', markersize=1.5,color = "green", label="Ff")
            part_ax_gen.plot(i+0.9,int(row[3]), marker='o', markersize=1.5,color = "blue", label="FF")
            part_ax_gen.plot(i+1,int(row[4]), marker='o', markersize=1.5,color = "black", label="totale")
    print("done gen {}".format(i))
            

for fichier in fichiers:
    fichier.close()
part_fig_homorec.savefig("homorec.png")
part_fig_hetero.savefig("hetero.png")
part_fig_homodom.savefig("homodom.png")
part_ax_gen.legend(loc="upper right")
part_fig_gen.savefig("gen.png")


