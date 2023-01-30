function search() {
    var input, filter, table, tr, a, b, c, d, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        a = tr[i].getElementsByTagName("td")[0];
        if (a) {
            txtValue = a.textContent || a.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                b = tr[i].getElementsByTagName("td")[1];
                if (b) {
                    txtValue = b.textContent || b.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    } else {
                        c = tr[i].getElementsByTagName("td")[2];
                        if (c) {
                            txtValue = c.textContent || c.innerText;
                            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                                tr[i].style.display = "";
                            } else {
                                d = tr[i].getElementsByTagName("td")[3];
                                if (d) {
                                    txtValue = d.textContent || d.innerText;
                                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                                    tr[i].style.display = "";
                                    } else {
                                    tr[i].style.display = "none";
                                    }
                                }       
                            }
                        }
                    }       
                }
            }
        }       
    }
}       