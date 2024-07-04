<!--% rebase('chinook_base.tpl', stylesheet='results_style')-->
% rebase('chinook_base.tpl')

<h1>{{ title }}</h1>
<p>{{ description }}</p>

% if len(records) < 1:
<p><strong>No records found</strong></p>
% else:
<table>
    <tr>
        % for field in records[0].keys():
        <th> {{ field }} </th>
        % end
    </tr>
    % for record in records:
    <tr>
        % for field in record:
        <td>{{ field }}</td>
        % end
    </tr>
    % end
</table>
%end
