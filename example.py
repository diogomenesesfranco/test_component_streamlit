import streamlit as st

import TabBar as tb

st.write("# Tab Bar")

chosen_id = tb.tab_bar(
    data=[
        tb.TabBarItemData(id=1, title="1", description="Tasks to take care of"),
        tb.TabBarItemData(id=2, title="2", description="Tasks taken care of"),
        tb.TabBarItemData(id=3, title="3", description="Tasks missed out askjdlaksjd lkaj sldkj al skjdlkaj sdlkj alskjd laksj dlakj sldkja lskdj alskjd laksjd l"),
    ],
    default=1,
    return_type=int,
)

st.info(f"chosen_id = {chosen_id}, type = {type(chosen_id)}")