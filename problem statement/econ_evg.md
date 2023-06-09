# Развитие “экономики”.

Основная картина видится так. Есть два основных пути

Первый - короткий. Его суть: допиливаем текущий расчет Димы Казанцева и встраиваем в него расчёт Жени со стоимостью замены насосов  как дополнение к What-IF.

Плюсы: достаточно быстро в базовой итерации, полезно для технологов (знают расходы на мероприятия), важно для ЦУДа в целом, одна из претензий экономистов (невозможность учета потерь электроэнергии, эту проблему решает модуль Тимура) снимается

Минусы: не работает на долгосрочную перспективу, неинтересно экономистам (а в будущем проекте именно с ними, в основном, предстоит работать). 
Остается все равно много удельных расходов (это еще одна претензия экономистов к текущему расчету). Без долгосрочных доработок, которые предполагаются в рамках ИПР ЦУД-2 это выглядит не так перспективно и “новаторски”. Еще это не очень похоже на “тизер”, о котором мы говорили в рамках предыдущих встреч, это скорее перенос имеющейся в Мегионе методики на нашу платформу с некоторыми полезными дополнениями.
На мой взгляд короткий путь тем не менее нуждается в реализации прежде чем мы будем подписывать новый договор и приступать к реализации второго проекта.

## Предлагается также “второй путь”

Его суть - разработка новой концепции с прицелом на новый договор. Ранее она частично показывалась тем же Тивольту и Кулемзину, принципиальных возражений от них услышано не было. 
От них было понимание, что эти разработки им нужны и они должны реализовываться.

Основные идеи такие.

Главная сложность - распределение не прямых, а косвенных затрат - например, на транспорт, обслуживание дорог и так далее. Предлагается решать эту проблему следующим способом.

На первом этапе расписываются статьи затрат в датакаде (от простой “базовой” физики до величины расходов по процессу в рамках месторождения. Эта физика может быть выражена как в форме неких промежуточных величин (например, машиносмен в месяц, либо силы тока) киловатт в час либо машиночасов - то есть, предмета оплаты. К этому предмету возможно привязать свой ID. Параллельно с этим идет разработка единой базы договоров, содержащих информацию о предмете закупки товара/услуги, подрядчиках, объемах, тарифах и пр. По каждому из этих предметов также будут присваиваться ID таким образом, что на следующем этапе объединения тарифов и закупаемых объемов мы будем делать условный join по соответствующим ID. Таким образом, будет возможет расчёт конкретных сумм в заданных статьях затрат и реализован принцип связки физики и экономики.

По сути, прописывание структуры затрат позволит прозрачно формировать производственные программы различных подразделений, когда они  с помощью подгрузки csv в датакад могут как планировать свои расходы, так и отражать факт уже понесенных расходов (будет достаточно указывать физические величины, поскольку уже будет выполнена связка с тарифами). Возможно несколько сценариев : модификация файла службы (как это уже было показано на демке в декабре), либо  разработка некоторых форм по потребностям служб, которые будут подгружаться в датакад. В свою очередь экономисты смогут видеть все эти схемы и прозрачно собирать информацию от всех подразделений к себе при необходимости. Также возможно построение общей схемы бюджета из статей затрат подразделений. То есть, цепочка такая Статья расходов → Расходы по подразделению (также возможно разбиение по процессу и месторождению) → Расходы по предприятию в целом. Экономистам больше интересно макропланирование, а то, что они хотят решить проблему корректного потока по скважине - об этом скажу позже.

Конкретный кейс  - планирование транспортных затрат (а их достаточно затруднительно распределить по скважине) с указанием конкретных мест выезда. Можно определить условный квадрат, в котором будет работать техника и распределить затраты на скважины, находящиеся в этом квадрате.

Другой кейс - планирование затрат на аренду и сервис УЭЦН. Эти расходы прямые, однако, бизнес процессы отлажены таким образом, выгрузки по часам работы насосов происходят раз в месяц. Кроме того, ведение учета достаточно запутано и происходит в нескольких файлах, перевязанных друг с другом, т.е нет какой-то единой системы с понятными источниками, не всегда возможно проверить корректность загружаемой информации. Цены также привязываются вручную, что усложняет расчет как для исполнителя, так и понимание этого расчёта экономистами. Привязка к тарифам уже автоматически убирает здесь часть проблем.
И электроэнергия с модулем Тимура. Здесь также понятно - знаем потребление насосов, знаем потери, знаем потребление прочих объектов на той же кустовой площадки - тогда  сможем более подробно считать УРЭ: не в рамках месторождения, а, например, в рамках соответствующего ДНС. Коме того, в дальнейшем можно реализовать возможность экономической целесообразности переключения с покупной э-э на генерацию и обратно (стоимость переключения, срок окупаемости и пр.) и выбор между продажей дополнительного объема газа либо его использованием его в целях генерации (если речь не идет на Тайлаках, там всё идет на генерацию). 

В целом, вся эта реализация будет полезна прежде всего экономистам. Но и мы получаем более точные уделки, т.к. Будут привязки не к месторождению, а к более узким зонам ответственности, например, типа ДНС. Таким образом, можно вернуться к первой истории и рассчитать более точные потоки на скважину таким образом, чтобы сумма этих расходов (с учётом распределяемых затрат) могла бы складываться в те агрегированные статьи (либо их суммы), которые привыкли видеть Тивольт и его команда в своих формах. Повторюсь, это им интересно, реализацию они видели на примере транспорта (достаточно подробную), предлагали попробовать с реальными специалистами. В своё время общались, запрос есть и от подразделений, так что проблем быть не должно. Но, наверное, уже не совсем в рамках пилота.