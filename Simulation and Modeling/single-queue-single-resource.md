# Single Queue Single Resource

This script generates single queue single resource simulation table. This simulation is also known as **Single-Channel Queue**.

## Script
<ul>
    <li>This script requires 4 input files; two <code>csv</code> files and two <code>txt</code> files.</li>
    <li>1st <code>csv</code> file contains <b>Time Between Arrival Distribution</b> table. And 2nd <code>csv</code> file contains <b>Service Time Distribution</b> table.</li>
    <li>1st <code>txt</code> file contains <b>Random Digits for Time Between Arrival</b>. And 2nd <code>txt</code> file contains <b>Random Digits for Servie Time</b>.</li>
    <li>Each data of <code>txt</code> file should be spearated by a single coma.</li>
</ul>

## Output
Full form of coulmn names-
<table>
    <tr>
        <th>Short Form</th> <th>Full Form</th>
    </tr>
    <tr>
        <td>RDA</td> <td>Random Digits for Arrival</td>
    </tr>
    <tr>
        <td>TSLA</td> <td>Time Since Last Arrival</td>
    </tr>
    <tr>
        <td>AT</td> <td>Arrival Time</td>
    </tr>
    <tr>
        <td>RDS</td> <td>Random Digits for Service</td>
    </tr>
    <tr>
        <td>ST</td> <td>Service Time</td>
    </tr>
    <tr>
        <td>TSB</td> <td>Time Service Begins</td>
    </tr>
    <tr>
        <td>TCWQ</td> <td>Time Customer Waits in Queue</td>
    </tr>
    <tr>
        <td>TSE</td> <td>Time Service Ends</td>
    </tr>
    <tr>
        <td>TCSS</td> <td>Time Customer Spends in System</td>
    </tr>
    <tr>
        <td>ITS</td> <td>Idle Time of System</td>
    </tr>
</table>

## Conclusion
This script only generates the simulation table. Other calculations need to done manually.
