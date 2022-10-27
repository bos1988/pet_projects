# Wordle
> **Беспроигрышная игра в Wordle (5 слов).**

<br/>

### Стек:

*Обработка данных<br/>Исследование<br/>Анализ данных*

### Используемые библиотеки:
*pandas<br/>Image<br/>collections*

### Результат работы:

1. В результате исследования и анализа слов найдена комбинация слов, позволяющая выигрывать в Wordle (5 слов) в 99,9% случаев
2. Составлен алгоритм, повышающий результативность игры в Wordle (5 слов)

### Рабочие файлы:
| Имя                                        | Описание                                                                           |
|:-------------------------------------------|:-----------------------------------------------------------------------------------|
| **wordle_search.ipynb**                    | Исследование-поиск универсальной победной комбинации слов                          |
| **wordle_play.ipynb**                      | Практическое применение во время игры в Wordle (5 слов) для гарантированной победы |
| **russian_nouns.txt**                      | Найденный в сети корпус русских слов                                               |
| **russian_nouns_e.txt.txt**                | Корпус русских слов с заменой `ё` на `е`                                           |

### Table of contents (wordle_search.ipynb):

<div class="toc"><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Библиотеки" data-toc-modified-id="Библиотеки-0.1"><span class="toc-item-num">0.1&nbsp;&nbsp;</span>Библиотеки</a></span></li></ul></li><li><span><a href="#Введение" data-toc-modified-id="Введение-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Введение</a></span><ul class="toc-item"><li><span><a href="#Описание-игры" data-toc-modified-id="Описание-игры-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Описание игры</a></span></li><li><span><a href="#Идея" data-toc-modified-id="Идея-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Идея</a></span></li></ul></li><li><span><a href="#Исследование" data-toc-modified-id="Исследование-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Исследование</a></span><ul class="toc-item"><li><span><a href="#Загрузка" data-toc-modified-id="Загрузка-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Загрузка</a></span></li><li><span><a href="#Подготовка" data-toc-modified-id="Подготовка-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Подготовка</a></span></li><li><span><a href="#Буквы" data-toc-modified-id="Буквы-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Буквы</a></span></li><li><span><a href="#Слова-с-уникальными-буквами" data-toc-modified-id="Слова-с-уникальными-буквами-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Слова с уникальными буквами</a></span></li><li><span><a href="#Обработка" data-toc-modified-id="Обработка-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Обработка</a></span></li><li><span><a href="#Основной-код-обработки" data-toc-modified-id="Основной-код-обработки-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Основной код обработки</a></span></li></ul></li><li><span><a href="#Вывод" data-toc-modified-id="Вывод-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Вывод</a></span></li></ul></div>