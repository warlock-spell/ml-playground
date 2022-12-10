# @Project:     LearnML
# @Filename:    linear_regression_page.py
# @Author:      Daksh
# @Time:        09-12-2022 11:52 pm

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
from src.component.page_layout import create_page_layout
import dash_bootstrap_components as dbc
from src.component.page_order import order

dash.register_page(__name__, title="Linear Regression", name="Linear Regression", order=["linear_regression_page"])
df = px.data.tips()
learn = dbc.Container("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eu arcu quis justo convallis tincidunt. Curabitur a orci eu nulla dapibus vehicula. Nullam semper orci non metus pharetra tincidunt. Donec iaculis vel justo quis auctor. Fusce in rutrum elit, et malesuada ex. Integer ut faucibus nisl. Phasellus convallis dolor id velit mollis ornare. Donec pharetra diam ac est laoreet rutrum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec euismod quis dui non gravida. Nullam quis diam accumsan, lobortis tellus at, pellentesque justo.

Sed felis tortor, malesuada et mattis placerat, placerat at dui. Mauris eu enim scelerisque, varius odio a, dapibus dolor. Aliquam eleifend felis diam, quis condimentum lacus ornare eu. Phasellus vulputate eros eget fermentum accumsan. Aliquam aliquam pharetra magna, vitae tincidunt leo aliquet ac. Etiam ac aliquet leo. Fusce vel mi blandit, tristique sem a, elementum lacus. Integer interdum ante a nulla elementum, et fringilla elit facilisis.

Aliquam in placerat sapien. Praesent sit amet urna vehicula, viverra ipsum sed, porttitor dolor. Duis vitae diam in dolor tempus luctus. Proin neque augue, bibendum vel blandit eu, vulputate a quam. Aenean semper, magna at euismod faucibus, enim purus suscipit augue, sit amet ornare erat erat sit amet ipsum. Mauris finibus hendrerit diam. Mauris mauris sapien, vehicula sit amet efficitur ut, consectetur a turpis. Vivamus egestas tincidunt viverra. Curabitur interdum nisi sagittis, semper eros ut, blandit metus. Phasellus vestibulum lobortis orci, in rutrum eros dictum sed. Donec efficitur convallis mi. Aliquam in turpis sit amet leo pellentesque pellentesque. Duis vel varius nisi, non pretium orci. Curabitur volutpat blandit erat vitae tempor.

Nunc eu magna luctus, congue odio id, hendrerit massa. Maecenas tempor porttitor faucibus. Quisque aliquet venenatis vulputate. Maecenas nulla magna, commodo at lorem ut, blandit porta justo. Nullam semper ultricies erat. Vivamus dolor justo, auctor quis posuere at, sodales sit amet elit. Nunc vehicula hendrerit ultrices. Sed aliquet, leo sit amet porta accumsan, dolor nunc mattis urna, in tempus arcu urna sed sapien.

Fusce sodales maximus neque. Etiam eu mollis sapien. Morbi in volutpat tellus. Donec ornare, nulla luctus maximus pellentesque, nisl elit congue orci, non accumsan orci sem at purus. Nullam libero lorem, dapibus at porttitor eu, suscipit at elit. Praesent ut magna quam. Phasellus sit amet malesuada mauris. Mauris convallis hendrerit felis et euismod. Quisque varius et felis non condimentum. Sed eu elementum sem, ut dapibus mauris. Nam nunc justo, efficitur ac finibus et, pulvinar a felis. Curabitur consectetur aliquet tortor, in placerat magna molestie eu. Donec cursus dictum tellus. Nullam magna quam, interdum eu leo nec, tempor semper arcu. Pellentesque sit amet maximus libero. Vivamus mi ligula, vulputate quis convallis nec, facilisis at leo.

Quisque vel imperdiet magna. Donec at diam et libero pellentesque auctor eu euismod tortor. Quisque a tortor velit. Curabitur nec consectetur libero. Maecenas convallis iaculis dictum. Suspendisse mollis massa eros, laoreet malesuada ex egestas sed. Nam eleifend nec libero sit amet tincidunt. Aliquam quis malesuada urna. Morbi eleifend elit feugiat, egestas magna id, cursus est. Duis commodo, risus vitae efficitur interdum, nulla dolor tincidunt lectus, sagittis malesuada enim est in ex. Fusce vulputate est a lacus pretium imperdiet. Donec placerat tristique nibh molestie vulputate. Praesent id vehicula erat. Nunc rhoncus justo feugiat odio tincidunt, eu semper elit vestibulum. Aliquam erat volutpat. Nulla fermentum metus ac nunc rutrum pretium.

Proin posuere enim ex, id lacinia sem luctus et. Duis sed sapien eu sapien congue ullamcorper. Praesent feugiat ac odio eu convallis. Aenean sagittis ipsum efficitur ipsum gravida, non viverra erat sollicitudin. Praesent hendrerit nec tellus vitae facilisis. Morbi consectetur lacus quam, at tempus sapien iaculis ac. Quisque efficitur nibh neque, consequat consequat quam pretium eu. Nunc risus augue, tempor a tortor non, auctor bibendum arcu. Fusce sed justo vel ligula posuere vehicula sed vestibulum purus. Praesent libero tellus, ullamcorper quis feugiat eu, consectetur non sem. Pellentesque vitae mattis quam, aliquet aliquet augue. Aliquam id fringilla risus, non scelerisque augue. Cras laoreet lorem eu tortor pellentesque sagittis. Pellentesque congue consequat tortor nec faucibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nec sodales metus.

Phasellus vitae vehicula nisl. Curabitur pulvinar, sapien sit amet semper consectetur, nulla lacus auctor dui, et euismod justo est sit amet justo. Quisque lectus ante, sodales in lorem nec, rhoncus suscipit urna. Suspendisse a rutrum ex. Duis pretium posuere felis, non eleifend nisi malesuada eget. Etiam mattis augue id viverra eleifend. Morbi ac ante a libero dictum porta. Curabitur ac hendrerit est, ac ultricies massa. Vestibulum eu orci a neque dignissim vulputate condimentum eu lorem. Fusce non laoreet lacus.

Sed ac velit vitae lacus scelerisque aliquet. Vestibulum dictum eros vitae odio pellentesque vestibulum. Ut ac erat vel ante accumsan sagittis. Suspendisse potenti. Etiam molestie mi sed magna sagittis, nec cursus urna vulputate. Vestibulum sem nisi, rhoncus non maximus eget, accumsan quis nisi. Curabitur ac suscipit eros. Aliquam ultrices eros metus, pretium euismod metus faucibus et. Phasellus pellentesque ante eu sem semper elementum. Nunc eu egestas mi. Quisque ut accumsan urna, in venenatis dolor. Praesent arcu tortor, ullamcorper nec venenatis vitae, malesuada eget neque.

In consequat ut odio vitae luctus. Vestibulum eu est tristique, consequat mi pellentesque, elementum odio. Morbi sit amet ligula eget nisl efficitur efficitur. Pellentesque vehicula dignissim euismod. Quisque ultricies, nisi ullamcorper laoreet bibendum, elit eros varius quam, eu sollicitudin nisi arcu imperdiet justo. Donec et consectetur ex. Phasellus facilisis fringilla odio nec euismod. Quisque magna felis, vehicula vehicula semper sit amet, vestibulum in dui. Curabitur feugiat facilisis purus, vel lacinia ante varius vel. Donec dignissim enim nunc, sed aliquet tortor scelerisque eu. Nulla bibendum laoreet feugiat. Nam imperdiet fringilla orci, euismod viverra dolor bibendum ac. Maecenas luctus viverra diam auctor rhoncus.

Aliquam bibendum non diam a sodales. Donec volutpat egestas dapibus. Maecenas mollis elit ut neque sagittis molestie. Aliquam placerat felis vitae velit congue commodo. Aenean non eros ac libero rutrum varius. Cras eros felis, viverra in lobortis ac, viverra pellentesque purus. Aenean erat mi, hendrerit placerat magna et, imperdiet lobortis tortor. Quisque in semper magna. Nullam fringilla, est quis lobortis convallis, sem odio finibus erat, iaculis vulputate dui nibh id arcu. Vestibulum accumsan dolor non mattis rhoncus. Vestibulum egestas congue metus, vel eleifend est fringilla in. Donec scelerisque faucibus lorem nec dictum. Sed vehicula finibus finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

Aenean sodales bibendum velit vulputate malesuada. Etiam facilisis nisl quis ante mattis interdum. Donec mattis, magna condimentum semper efficitur, erat erat pharetra ligula, quis pharetra nunc purus id tellus. Pellentesque volutpat, lacus ac maximus gravida, sem erat convallis ligula, sed dapibus lorem turpis eu leo. Maecenas viverra tincidunt bibendum. Quisque est nulla, pharetra sit amet massa nec, egestas porttitor nunc. Morbi commodo elit sit amet fermentum rhoncus. Nunc lacinia nibh est, ac sodales massa consequat sed.

Cras facilisis, ante non tincidunt facilisis, nisi eros dignissim mi, at mollis leo ipsum ac neque. Proin non commodo nisl. Cras placerat quis elit eget rutrum. Donec venenatis urna id sapien elementum, eu vestibulum augue bibendum. Integer faucibus ante neque, nec porta ex tempus nec. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis et turpis quis urna condimentum blandit.

Aenean a dolor eleifend, lobortis risus vel, venenatis nisl. Praesent bibendum ullamcorper nisl eget ornare. Suspendisse at tincidunt dolor. Vestibulum eget tincidunt nisl. Sed non fringilla mi, vitae rhoncus lacus. In quis mollis quam. Phasellus condimentum ac dolor vel commodo. In in maximus tortor, sed sodales est. Fusce ac blandit magna, vitae tempor metus. Vivamus molestie euismod erat, vitae semper ex rutrum sed. Morbi feugiat a felis sed elementum. Sed vitae placerat metus, id blandit orci. Sed feugiat felis mauris, eu posuere quam euismod in. Fusce volutpat ex tortor, in eleifend sapien aliquet eu.

Nulla ultricies at mi a convallis. Sed sodales tortor lacus, et volutpat tellus faucibus vel. Suspendisse potenti. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris sit amet egestas tortor, sit amet porta diam. Ut a aliquam eros. Praesent sagittis, arcu non convallis pharetra, turpis eros vehicula massa, quis sollicitudin sem velit molestie ligula. Nam eros neque, commodo id magna aliquam, lacinia maximus nisl. Cras consequat lacinia rutrum. Fusce ac sem ultricies, pellentesque turpis id, convallis felis. Nullam pretium placerat lorem sed ultricies. Vestibulum volutpat nisi non nunc fermentum, quis consectetur diam sagittis. Morbi sit amet purus laoreet, scelerisque urna et, fermentum velit. In feugiat tortor vel faucibus vulputate.

Integer varius interdum purus a malesuada. Sed pulvinar dolor ac posuere aliquet. Etiam at leo euismod, tincidunt elit at, imperdiet massa. Donec convallis nibh vitae ligula vehicula, sit amet iaculis leo dictum. Suspendisse laoreet orci magna, eget vulputate elit congue quis. Quisque maximus imperdiet risus, ac finibus purus fringilla ut. Nullam ultrices consectetur lectus sit amet iaculis. Quisque ornare risus aliquam augue hendrerit aliquet. Proin tempor id ipsum vel molestie. Proin non iaculis eros. Sed posuere felis enim, at commodo sem blandit a. Sed dapibus efficitur lorem, in tincidunt ligula porta sed. Proin ipsum nisl, sollicitudin ac risus id, molestie consectetur velit. Mauris et turpis mollis, gravida turpis ut, euismod mi.

Quisque faucibus pretium cursus. Suspendisse mattis ullamcorper massa, quis mollis ipsum. Nulla facilisis congue lacus non rutrum. Sed augue mi, porttitor ac sem nec, facilisis tristique metus. Duis dignissim turpis sit amet turpis facilisis, a luctus libero suscipit. Fusce lectus turpis, tincidunt sed euismod vel, convallis vel lacus. Pellentesque non pulvinar tortor. Phasellus cursus, orci et ullamcorper condimentum, nisl turpis tincidunt odio, in viverra magna diam sed mauris. Curabitur blandit justo sit amet nunc sagittis, non scelerisque magna ultricies. Duis pretium leo ac bibendum consectetur.

Maecenas pharetra eget sapien ac malesuada. In ornare lectus eleifend vulputate porta. Fusce in tellus blandit, hendrerit metus id, sodales sapien. Fusce auctor pulvinar hendrerit. Donec sit amet congue erat. Suspendisse sagittis cursus nunc. Donec gravida, nunc sit amet vulputate laoreet, dolor lacus facilisis quam, at pharetra orci est vitae nibh. Suspendisse mattis purus ut ante porttitor, non rhoncus orci scelerisque. Donec eleifend quis eros vel aliquam. Etiam dignissim, orci nec porttitor dignissim, est ligula molestie tellus, elementum posuere purus augue et tellus. Suspendisse mi felis, facilisis sit amet dolor in, consequat varius nunc. Cras consequat nisl id nisi malesuada hendrerit. Quisque hendrerit pellentesque feugiat. Nunc viverra sagittis varius. Aenean auctor purus in dui condimentum tincidunt.

Vivamus id lectus quis velit malesuada fringilla quis semper odio. Aliquam id lorem vulputate, efficitur nisl sed, fringilla justo. Sed tincidunt tortor eget leo ultrices, id semper nulla molestie. In sodales dui sed malesuada gravida. Vestibulum eget ipsum lectus. Maecenas massa metus, varius quis nisl id, suscipit mollis felis. In aliquam, orci tristique feugiat pellentesque, neque arcu faucibus metus, gravida elementum enim lacus ac ipsum. Vivamus in vestibulum ligula, eu elementum ante. Donec sit amet pulvinar ex, et elementum diam. Nullam sem nisl, rhoncus hendrerit porta vitae, lacinia sollicitudin felis. Nunc fermentum semper nibh, quis semper est ultrices et.

Cras suscipit, ligula sit amet ultricies interdum, lorem justo tincidunt arcu, a gravida ligula elit ac dui. Quisque vehicula diam ac lacus faucibus, a feugiat elit dictum. In mollis arcu et ligula aliquet commodo. Curabitur euismod mauris orci, quis sodales magna bibendum in. Nam elementum feugiat erat, vel tristique lectus porta et. Nunc vitae nibh sit amet risus pretium mattis vitae eget ligula. Suspendisse potenti. Fusce sit amet massa eget orci porttitor ullamcorper quis vel tortor. Etiam ornare, leo nec tincidunt auctor, sem enim bibendum risus, nec bibendum augue felis vel ipsum. Proin sapien purus, posuere at arcu vel, feugiat viverra justo. Praesent pretium nunc vel metus commodo, rhoncus volutpat tellus pretium. Nunc at neque in tortor maximus lobortis. Fusce vitae hendrerit urna.""")
play = dbc.Container(html.Div(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.Img(src='assets/smoking2.jpg')
                ], width=4
            ),
            dbc.Col(
                [
                    dcc.RadioItems(df.day.unique(), id='day-choice', value='Sat')
                ], width=6
            )
        ]),
        dbc.Row([
            dbc.Col(
                [
                    dcc.Graph(id='bar-fig',
                              figure=px.bar(df, x='smoker', y='total_bill'))
                ], width=12
            )
        ])
    ]
))


@callback(
    Output('bar-fig', 'figure'),
    Input('day-choice', 'value')
)
def update_graph(value):
    dff = df[df.day == value]
    fig = px.bar(dff, x='smoker', y='total_bill')
    return fig


layout = create_page_layout(learn_tab=learn, play_tab=play)
