# Single Queue Double Resource

This script generates single queue double resource simulation table. This simulation is also known as **The Able Baker Carhop Problem**.

## Script
<ul>
    <li>This script requires 5 input files; three <code>csv</code> files and two <code>txt</code> files.</li>
    <li>1st <code>csv</code> file contains <b>Time Between Arrival Distribution</b> table. 2nd <code>csv</code> file contains <b>Service Time Distribution</b> table of higher priority resource. And 3rd <code>csv</code> file contains <b>Service Time Distribution</b> table of lower priority resource.</li>
    <li>1st <code>txt</code> file contains <b>Random Digits for Time Between Arrival</b>. And 2nd <code>txt</code> file contains <b>Random Digits for Servie Time</b>.</li>
    <li>Each data of <code>txt</code> files should be spearated by a single coma.</li>
</ul>

## Output
Full form of coulmn names-
<table>
    <tr>
        <th>Short Form</th> <th>Full Form</th>
    </tr>
    <tr>
        <td>CN.</td> <td>Customer No.</td>
    </tr>
    <tr>
        <td>RDA</td> <td>Random Digits for Arrival</td>
    </tr>
    <tr>
        <td>TBA</td> <td>Time Between Arrival</td>
    </tr>
    <tr>
        <td>CTA</td> <td>Clock Time Arrival</td>
    </tr>
    <tr>
        <td>RDS</td> <td>Random Digits for Service</td>
    </tr>
    <tr>
        <td>TSB(HP)</td> <td>Time Service Begins(Higher Priority)</td>
    </tr>
    <tr>
        <td>ST(HP)</td> <td>Service Time(Higher Priority)</td>
    </tr>
    <tr>
        <td>TSE(HP)</td> <td>Time Service Ends(Higher Priority)</td>
    </tr>
    <tr>
        <td>TSB(LP)</td> <td>Time Service Begins(Lower Priority)</td>
    </tr>
    <tr>
        <td>ST(LP)</td> <td>Service Time(Lower Priority)</td>
    </tr>
    <tr>
        <td>TSE(LP)</td> <td>Time Service Ends(Lower Priority)</td>
    </tr>
    <tr>
        <td>TQ</td> <td>Time in Queue(Lower Priority)</td>
    </tr>

</table>

## Conclusion
This script only generates the simulation table. Other calculations need to done manually.
