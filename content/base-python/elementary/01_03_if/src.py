import ipywidgets as widgets
from IPython.display import display, HTML

def alarm_clock():
    
    # Create a text box widget with a small width
    fill_in_blank = widgets.TimePicker(
        placeholder='Enter time', 
        layout=widgets.Layout(width='500px', display='inline-block'))
    
    # Create an HTML container with inline styling
    container = widgets.HBox([widgets.HTML("I wake up at "), fill_in_blank], layout=widgets.Layout(width='1000px'))
    
    # Display the inline sentence with the widget
    display(container)

    return fill_in_blank


def lunch():
    
    # Create a text box widget with a small width
    fill_in_blank = widgets.Dropdown(
    options=['cheeseburger', 'glass of water'],
    layout=widgets.Layout(width='500px', display='inline-block')
    )
    
    # Create an HTML container with inline styling
    container = widgets.HBox([widgets.HTML("For lunch I had a "), fill_in_blank])
    
    # Display the inline sentence with the widget
    display(container)

    return fill_in_blank


def time():

    # Create a text box widget with a small width
    fill_in_blank = widgets.TimePicker(placeholder='Enter time', layout=widgets.Layout(width='500px', display='inline-block'))
    
    # Create an HTML container with inline styling
    container = widgets.HBox([widgets.HTML("The time is "), fill_in_blank])
    
    # Display the inline sentence with the widget
    display(container)

    return fill_in_blank


def reset_button():
    from IPython.display import display, HTML
    display(HTML("""
    <style>
    .reset {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}
 .reset-hover {
  background-color: white; 
  color: black; 
  border: 2px solid #f44336;
}</style>
    <button type="button" class="reset reset-hover" id="button_for_indexeddb">Reset Notebook</button>
    <script>
    window.button_for_indexeddb.onclick = function(e) {
        window.indexedDB.open('JupyterLite Storage').onsuccess = function(e) {
            // There are also other tables that I'm not clearing:
            // "counters", "settings", "local-storage-detect-blob-support"
            let tables = ["checkpoints", "files"];
    
            let db = e.target.result;
            let t = db.transaction(tables, "readwrite");
    
            function clearTable(tablename) {
                let st = t.objectStore(tablename);
                st.count().onsuccess = function(e) {
                    console.log("Deleting " + e.target.result + " entries from " + tablename + "...");
                    st.clear().onsuccess = function(e) {
                        console.log(tablename + " is cleared!");
                    }
                }
            }
    
            for (let tablename of tables) {
                clearTable(tablename);
            }
        }
        location.reload();
    };
    </script>
    """))

