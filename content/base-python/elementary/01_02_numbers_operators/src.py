from ipycanvas import Canvas, hold_canvas
from time import sleep

def canvas(fill_style='orange'):
    global c 
    
    c = Canvas(width=1000, height=300)
    
    c.fill_style = fill_style
    
    c.fill_rect(0, 0, 1000, 600)

    return c


def write_message(message):
    
    message_ = str(message)
    # Number of steps in your animation
    steps_number = 200
    
    # Note how `hold_canvas` now wraps the entire for-loop
    with hold_canvas():
        for i in range(len(message_)):
            # Clear the old animation step
            fill_style = c.fill_style
            c.clear()
            c.fill_style = fill_style
            c.fill_rect(0, 0, 1000, 600)
    
            c.fill_style = 'white'
            c.font = "80px serif"
    
            c.fill_text(message_[:i + 1], 20, 180)

            c.fill_style = fill_style
    
            # Animation frequency ~50Hz = 1000./50. milliseconds
            c.sleep(50)


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
