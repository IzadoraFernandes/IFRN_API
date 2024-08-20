# Generated by Django 5.0.7 on 2024-07-17 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_autor', models.CharField(max_length=250, verbose_name='Autor')),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=50, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_editora', models.CharField(max_length=250, verbose_name='Editora')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_livro', models.CharField(max_length=100, verbose_name='Nome do Livro')),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('data_lancamento', models.DateField(verbose_name='Data de Lançamento')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('descricao_livro', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descrição do Livro')),
                ('cover', models.ImageField(upload_to='livros/cover/%Y/%m/%d/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.autor', verbose_name='Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.categoria', verbose_name='Categoria')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.editora', verbose_name='Editora')),
            ],
        ),
    ]
