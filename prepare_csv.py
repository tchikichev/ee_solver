#%%
import pandas as pd
import os


# loc = "v2_dtcd_read_graph_ee_fill_props_3.csv"
loc = "dtcd_read_graph_ee_fill_props_test.json.csv"
writeTo = '.'.join(loc.split('.')[:-1])

#%%

# df = pd.read_csv(loc, index_col=False)
# df.head()

# | readFile format=json path=dtcd_read_graph_ee_fill_props_test.json
# | spath input=properties output=object_type path=object_type.value
# | spath input=properties output=isActive path=isActive.value
# | eval properties = "'" + properties + "'"
# | eval source_edges = "'" + source_edges + "'"
# | eval target_edges = "'" + target_edges + "'"
# | eval initPorts = "'" + initPorts + "'"
# query
#%%
import json

df = pd.read_csv(
    loc,
    converters={
        'properties': json.loads,
        'source_edges': json.loads,
        'target_edges': json.loads,
        'initPorts': json.loads
    },
    header=0,
    quotechar="'")

df.head()
# # %%
# stest = 
# '[{"primitiveName": "outPort1", "type": ["OUT"], "properties": {"status": {"expression": "", "type": "expression", "status": "complete", "value": ""}}, "location": {"x": 14348, "y": 3022.7}, "primitiveID": "esOut_2568_outPort1"}, {"primitiveName": "inPort1", "type": ["IN"], "properties": {"status": {"expression": "", "type": "expression", "status": "complete", "value": ""}}, "location": {"x": 14367.5, "y": 3021.7}, "primitiveID": "esOut_2568_inPort1"}]',
# esOut_2568,
# esOut,
# '{"description": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "normallylnService": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "model": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "Name": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "object_type": {"type": "expression", "expression": "\"unknown_cons\"", "status": "complete", "value": "unknown_cons"}, "zagruzka": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "current": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "kV": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "power": {"expression": "", "type": "expression", "status": "complete", "value": ""}, "name": {"type": "expression", "expression": "\"unknown_cons \u041a\u0422\u041f\u041d 6/0,4 \u043a\u0412 630 \u043a\u0412\u0410 \u21162 \u041a\u041f-1\"", "status": "complete", "value": "unknown_cons \u041a\u0422\u041f\u041d 6/0,4 \u043a\u0412 630 \u043a\u0412\u0410 \u21162 \u041a\u041f-1"}, "source": {"type": "expression", "expression": "\"pokup\"", "status": "complete", "value": "pokup"}, "parent_name": {"type": "expression", "expression": "\"\u0441/\u0440 \u211610 \u041f\u0421 35/6 \u043a\u0412 \u0410\u0431\u0430\u0437\u0430\u0440\u043e\u0432, \u0422\u0420-\u0440 35/6 \u043a\u0412 \u21162 (\u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u0438\u043f \u0442\u0440-\u0440\u0430; ; 0) nan \u041a\u0422\u041f\u041d 6/0,4 \u043a\u0412 630 \u043a\u0412\u0410 \u21162 \u041a\u041f-1\"", "status": "complete", "value": "\u0441/\u0440 \u211610 \u041f\u0421 35/6 \u043a\u0412 \u0410\u0431\u0430\u0437\u0430\u0440\u043e\u0432, \u0422\u0420-\u0440 35/6 \u043a\u0412 \u21162 (\u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0442\u0438\u043f \u0442\u0440-\u0440\u0430; ; 0) nan \u041a\u0422\u041f\u041d 6/0,4 \u043a\u0412 630 \u043a\u0412\u0410 \u21162 \u041a\u041f-1"}, "power_kWh": {"type": "expression", "expression": "", "status": "complete", "value": ""}, "power_coef": {"type": "expression", "expression": "1", "status": "complete", "value": 1}}',
# '[]',
# '[{"bends": [[14457.5, 2893.2], [14367.5, 2955.2]], "sourceNode": "eeKTPN_1928", "targetNode": "esOut_2568", "extensionName": "ExtensionCommonPrimitives", "primitiveName": "SimpleEdge", "sourcePort": "eeKTPN_1928_outPort1", "targetPort": "esOut_2568_inPort1"}]',
# unknown_cons,
# None

#%%
loc = "dtcd_read_graph_ee_fill_props_test.json.xltx"

pd.read_excel(
    loc,
    header=0,
    index_col=False,
    converters={'properties': json.loads, 'source_edges': json.loads, 'target_edges': json.loads, 'initPorts': json.loads})
# %%
df = pd.read_excel(
    loc,
    header=0,
    index_col=False)

df['properties'].apply(lambda x: json.load(x))

# %%
loc = "dtcd_read_graph_ee_fill_props_test2.json.csv"
df = pd.read_csv(
    loc,
    sep=";",
    # converters={
    #     'properties': json.loads
    #     # 'source_edges': json.loads,
    #     # 'target_edges': json.loads,
    #     # 'initPorts': json.loads
    # },
    header=0,
    quotechar="'",
    usecols=list(range(8)))
df.head()
# %%

def parse_column(data):
    try:
        return json.loads(data)
    except Exception as e:
        print(e)
        return None

df2 = pd.read_csv(
    loc, sep=";",
    converters={
        'properties': parse_column,
        'source_edges': parse_column,
        'target_edges': parse_column,
        'initPorts': parse_column
    },
    header=0,
    quotechar="'",
    usecols=list(range(8)),
    encoding = "utf-8"
)
df2.head()
# df = pd.read_csv('data/file.csv', converters={'json_column_name': parse_column})
# %%
df2.head()
# %%
import networkx as nx
import pandas as pd
import numpy as np
from os import path


object_types = {'BreakerOn',
 'DataLakeNode',
 'UncontrolledRichLabelNode01',
 'eeCableLine110Kv',
 'eeCableLine35Kv',
 'eeCableLine6Kv',
 'eeIn',
 'eeKTPN',
 'eeKru',
 'eeKrun',
 'eeOut',
 'eeRu',
 'eeStation',
 'eeSubstation',
 'eeTapConnector',
 'eeZru',
 'esOut',
 'oil_well'}


def make_ee_schema_from_dfs(
        dfs
        # row_type_col="row_type"
        ):
    df_nodes = dfs['nodes']
    df_edges = dfs['edges']
    # df_kns_pumps = dfs.get('kns_pumps', None)
    # df_well_pumps = dfs.get('well_pumps', None)
    # df_inclination = dfs.get('inclination', None)
    # df_HKT = dfs.get('HKT', None)

    objects_in = {}
    objects_out = {}
    juncs = {}

    # select noedes by type

    # prepare nodes

    # add to graph

    # add edges to graph

    # get incidence table, write equations

    # compute kirkhoff sum ...
    # sum of joints, loss elements

    # component equations at generation

    

    # all_nodes = {**objects_in, **objects_out, **juncs}

    # inlets.update({source_id: source_obj})


    # for row in outletsdf.itertuples():
    #     sink_id = row.node_id_end
    #     sink_obj = vrtxs.HE2_Boundary_Vertex(row.endKind, row.endValue)
    #     outlets.update({sink_id : sink_obj})


    G = nx.MultiDiGraph()  # Di = directed
    df_to_graph_edges_mapping = dict()
    
    for id, obj in dfs.items():
        # TODO:: add only node objects ??
        G.add_node(id, obj=obj)

    for id, obj in dfs.items():
        edges = obj['target_edges']
        for ei in edges:
            start = ei['sourceNode']
            end = ei['targetNode']
            k = G.add_edge(start, end, obj=obj)

        # G.add_node(id, obj=obj)

    # for k, v in {**inlets, **outlets, **juncs}.items():
    #     G.add_node(k, obj=v)

    # col_indexes = {col: idx for idx, col in enumerate(list(calc_df), start=1)}
    # row_type_idx = col_indexes[row_type_col]

    # for row in calc_df.itertuples():
    #     ...

    #     k = G.add_edge(start, end, obj=obj)  # edge index in MultiDiGraph. k in G[u][v][k] index
    #     df_to_graph_edges_mapping[row.Index] = (start, end, k)

    # cmpnts = nx.algorithms.components.number_weakly_connected_components(G)
    # if cmpnts != 1:
    #     logger.error(f"Not single componented graph!")
    #     raise ValueError

    return G, calc_df, df_to_graph_edges_mapping